// Import necessary modules
import express from 'express';
import redis from 'redis';
import kue from 'kue';
import { promisify } from 'util';

// Create Redis client and promisify necessary functions
const client = redis.createClient();
const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

// Create Kue queue
const queue = kue.createQueue();

// Variables for seat management
let reservationEnabled = true;
const initialAvailableSeats = 50;

// Function to set the initial number of available seats
async function reserveSeat(number) {
  await setAsync('available_seats', number);
}

// Function to get the current number of available seats
async function getCurrentAvailableSeats() {
  const seats = await getAsync('available_seats');
  return seats ? parseInt(seats) : 0;
}

// Initialize the number of available seats and reservation state
reserveSeat(initialAvailableSeats);

// Create an express app
const app = express();
const PORT = 1245;

// Route to get the number of available seats
app.get('/available_seats', async (req, res) => {
  const numberOfAvailableSeats = await getCurrentAvailableSeats();
  res.json({ numberOfAvailableSeats });
});

// Route to reserve a seat
app.get('/reserve_seat', async (req, res) => {
  if (!reservationEnabled) {
    return res.json({ status: 'Reservation are blocked' });
  }

  const job = queue.create('reserve_seat', {}).save(err => {
    if (err) {
      return res.json({ status: 'Reservation failed' });
    }
    res.json({ status: 'Reservation in process' });
  });

  job.on('complete', () => {
    console.log(`Seat reservation job ${job.id} completed`);
  });

  job.on('failed', err => {
    console.log(`Seat reservation job ${job.id} failed: ${err.message}`);
  });
});

// Route to process the queue
app.get('/process', (req, res) => {
  res.json({ status: 'Queue processing' });

  queue.process('reserve_seat', async (job, done) => {
    const currentAvailableSeats = await getCurrentAvailableSeats();
    if (currentAvailableSeats <= 0) {
      reservationEnabled = false;
      return done(new Error('Not enough seats available'));
    }

    const newAvailableSeats = currentAvailableSeats - 1;
    await reserveSeat(newAvailableSeats);

    if (newAvailableSeats === 0) {
      reservationEnabled = false;
    }

    done();
  });
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
