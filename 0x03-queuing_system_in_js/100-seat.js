import redis from 'redis';
import kue from 'kue';
import { promisify } from 'util';
import express from 'express';

// Create a Redis client
const client = redis.createClient();

// Promisify the get and set methods from the Redis client
const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

// Initialize the number of available seats and reservationEnabled
let reservationEnabled = true;
setAsync('available_seats', 50);

// Function to reserve a seat
const reserveSeat = async (number) => {
  if (reservationEnabled) {
    await setAsync('available_seats', number);
  }
}

// Function to get the current number of available seats
const getCurrentAvailableSeats = async () => {
  const seats = await getAsync('available_seats');
  if (seats <= 0) {
    reservationEnabled = false;
  }
  return seats;
}


const queue = kue.createQueue();

// Create an Express server
const app = express();
app.listen(1245, () => {
  console.log('Server listening on port 1245');
});

// Route to get the number of available seats
app.get('/available_seats', async (req, res) => {
  const seats = await getCurrentAvailableSeats();
  res.json({ numberOfAvailableSeats: seats });
});

// Route to reserve a seat
app.get('/reserve_seat', (req, res) => {
  if (!reservationEnabled) {
    res.json({ status: 'Reservations are blocked' });
    return;
  }

  const job = queue.create('reserve_seat', {}).save((err) => {
    if (err) {
      res.json({ status: 'Reservation failed' });
      return;
    }
    res.json({ status: 'Reservation in process' });
  });

  job.on('complete', () => {
    console.log(`Seat reservation job ${job.id} completed`);
  }).on('failed', (errorMessage) => {
    console.log(`Seat reservation job ${job.id} failed: ${errorMessage}`);
  });
});


// Route to process the queue
app.get('/process', async (req, res) => {
    res.json({ status: 'Queue processing' });
  
    queue.process('reserve_seat', async (job, done) => {
      let seats = await getCurrentAvailableSeats();
      if (seats > 0) {
        await reserveSeat(seats - 1);
        seats = await getCurrentAvailableSeats();
        if (seats === 0) {
          reservationEnabled = false;
        }
        done();
      } else {
        done(new Error('Not enough seats available'));
      }
    });
  });
  