import kue from 'kue';

/**
 * Creates jobs in the Kue queue
 * @param {Array} jobs - Array of job objects containing phoneNumber and message
 * @param {Object} queue - Kue queue instance
 */
function createPushNotificationsJobs(jobs, queue) {
  // Check if jobs is an array
  if (!Array.isArray(jobs)) {
    throw new Error('Jobs is not an array');
  }

  // Iterate over each job and add it to the queue
  jobs.forEach((jobData) => {
    // Create a job in the queue
    const job = queue.create('push_notification_code_3', jobData);

    // Log job creation
    job.on('enqueue', () => {
      console.log(`Notification job created: ${job.id}`);
    });

    // Log job completion
    job.on('complete', () => {
      console.log(`Notification job ${job.id} completed`);
    });

    // Log job failure
    job.on('failed', (errorMessage) => {
      console.log(`Notification job ${job.id} failed: ${errorMessage}`);
    });

    // Log job progress
    job.on('progress', (progress) => {
      console.log(`Notification job ${job.id} ${progress}% complete`);
    });

    // Save the job to the queue
    job.save();
  });
}

export default createPushNotificationsJobs;
