import createPushNotificationsJobs from './8-job.js';
import kue from 'kue';
import { expect } from 'chai';

const queue = kue.createQueue();

describe('createPushNotificationsJobs', () => {
  beforeEach(() => {
    queue.testMode.enter();
  });

  afterEach(() => {
    queue.testMode.clear();
    queue.testMode.exit();
  });

  it('should display an error message if jobs is not an array', () => {
    const notAnArray = 'notAnArray';
    expect(() => {
      createPushNotificationsJobs(notAnArray, queue);
    }).to.throw(Error, 'Jobs is not an array');
  });

  it('should create jobs in the queue', () => {
    const jobs = [
      { phoneNumber: '1234567890', message: 'Hello' },
      { phoneNumber: '0987654321', message: 'World' },
    ];
    createPushNotificationsJobs(jobs, queue);
    expect(queue.testMode.jobs.length).to.equal(2);
  });
});
