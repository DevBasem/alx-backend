import redis from 'redis';

// Create a Redis client
const client = redis.createClient();

// Handle connection and error events
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.error('Redis client not connected to the server:', err.message);
});

// Define a function to create a hash in Redis
const createHash = () => {
  const hashKey = 'HolbertonSchools';
  const schools = {
    Portland: '50',
    Seattle: '80',
    'New York': '20',
    Bogota: '20',
    Cali: '40',
    Paris: '2'
  };

  for (const [field, value] of Object.entries(schools)) {
    client.hset(hashKey, field, value, redis.print);
  }
};

// Define a function to display the hash from Redis
const displayHash = () => {
  const hashKey = 'HolbertonSchools';

  client.hgetall(hashKey, (err, result) => {
    if (err) {
      console.error('Error fetching hash:', err.message);
    } else {
      console.log(result);
    }
    client.quit();
  });
};

// Execute the functions
createHash();
displayHash();
