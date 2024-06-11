import { createClient } from 'redis';
import { promisify } from 'util';
import redis from 'redis';

const client = createClient();

client.on('error', err => console.log(`Redis client not connected to the server: ${err}`));
client.on('connect', () => console.log('Redis client connected to the server'));

const setNewSchool = (schoolName, value) => {
  client.set(schoolName, value, redis.print);
}

const getAsync = promisify(client.get).bind(client)

const displaySchoolValue = async (schoolName) => {
  const value = await getAsync(schoolName);
  console.log(value);
}


displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
