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

// Create a job object
const jobData = {
  phoneNumber: '123-456-7890',
  message: 'Hello, this is a notification!'
};

// Add a job to the queue
const job = queue.create('push_notification_code', jobData)
  .save((err) => {
    if (err) {
      console.error('Failed to create job:', err);
    } else {
      console.log(`Notification job created: ${job.id}`);
    }
  });

// Event listeners for job completion and failure
job.on('complete', () => {
  console.log('Notification job completed');
});

job.on('failed', (errorMessage) => {
  console.error(`Notification job failed: ${errorMessage}`);
});
