import { expect } from 'chai';
import kue from 'kue';
import createPushNotificationsJobs from './8-job.js';

// Create a test queue
const queue = kue.createQueue();

describe('createPushNotificationsJobs', () => {
  // Enter test mode before running the tests
  before(() => {
    queue.testMode.enter();
  });

  // Exit test mode and clear the queue after tests
  after(() => {
    queue.testMode.exit();
  });

  // Clear the test queue before each test
  beforeEach(() => {
    queue.testMode.clear();
  });

  it('should display an error message if jobs is not an array', () => {
    expect(() => createPushNotificationsJobs('invalid_jobs', queue)).to.throw('Jobs is not an array');
  });

  it('should create two new jobs to the queue', () => {
    const jobs = [
      {
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account',
      },
      {
        phoneNumber: '4153518781',
        message: 'This is the code 4562 to verify your account',
      },
    ];

    createPushNotificationsJobs(jobs, queue);
    
    expect(queue.testMode.jobs.length).to.equal(2);
    expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
    expect(queue.testMode.jobs[0].data).to.eql(jobs[0]);
    expect(queue.testMode.jobs[1].data).to.eql(jobs[1]);
  });
});
