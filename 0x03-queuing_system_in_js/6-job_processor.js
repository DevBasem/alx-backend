import kue from 'kue';
import redis from 'redis';

// Create a Redis client
const redisClient = redis.createClient();

// Create a Kue queue using the Redis client
const queue = kue.createQueue({
  redis: {
    host: '127.0.0.1',
    port: 6379
  }
});

// Function to send notification
function sendNotification(phoneNumber, message) {
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}

// Process jobs in the queue
queue.process('push_notification_code', (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message);
  done();
});
