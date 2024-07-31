import redis from 'redis';
import { promisify } from 'util';

// Create a Redis client
const client = redis.createClient();

// Handle connection and error events
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.error('Redis client not connected to the server:', err.message);
});

// Promisify the Redis client methods
const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

// Function to set a new school value in Redis
const setNewSchool = async (schoolName, value) => {
  try {
    const reply = await setAsync(schoolName, value);
    console.log('Reply:', reply);
  } catch (err) {
    console.error('Error setting value:', err.message);
  }
};

// Function to display the school value from Redis
const displaySchoolValue = async (schoolName) => {
  try {
    const reply = await getAsync(schoolName);
    console.log(reply);
  } catch (err) {
    console.error('Error fetching value:', err.message);
  }
};

// Call the functions
const main = async () => {
  await displaySchoolValue('Holberton');
  await setNewSchool('HolbertonSanFrancisco', '100');
  await displaySchoolValue('HolbertonSanFrancisco');
  client.quit();
};

main();
