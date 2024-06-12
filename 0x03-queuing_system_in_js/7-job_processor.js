import kue from 'kue';

const queue = kue.createQueue();

const blacklistedNumbers = [
  '1234567899',
  '1234567898',
  '1234567897',
  '1234567896',
  '1234567895',
  '1234567894',
  '4153518780',
  '4153518781'
]
const sendNotification = (phoneNumber, message, job, done) => {
    job.progress(0, 100);
    if (blacklistedNumbers.includes(phoneNumber)) {
    console.log(`Notification job #${job.id} failed: Phone number ${phoneNumber} is blacklisted`);
      done(new Error(`Phone number ${phoneNumber} is blacklisted`));
    }
    else {
      job.progress(50, 100);
      console.log(`Notification job #${job.id} 50% complete`);
      console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
      done();
      console.log(`Notification job #${job.id} completed`);
    }
}

queue.process('push_notification_code_2', 2, (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message, job, done);
});
