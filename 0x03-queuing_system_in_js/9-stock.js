// Import necessary modules
import express from 'express';
import redis from 'redis';
import { promisify } from 'util';
import bodyParser from 'body-parser';

// Create Redis client
const client = redis.createClient();
const getAsync = promisify(client.get).bind(client);

// List of products
const listProducts = [
  { itemId: 1, itemName: 'Suitcase 250', price: 50, initialAvailableQuantity: 4 },
  { itemId: 2, itemName: 'Suitcase 450', price: 100, initialAvailableQuantity: 10 },
  { itemId: 3, itemName: 'Suitcase 650', price: 350, initialAvailableQuantity: 2 },
  { itemId: 4, itemName: 'Suitcase 1050', price: 550, initialAvailableQuantity: 5 },
];

// Get item by ID
function getItemById(id) {
  return listProducts.find(item => item.itemId === parseInt(id));
}

// Reserve stock by ID
function reserveStockById(itemId, stock) {
  client.set(`item.${itemId}`, stock);
}

// Get current reserved stock by ID
async function getCurrentReservedStockById(itemId) {
  const stock = await getAsync(`item.${itemId}`);
  return stock ? parseInt(stock) : null;
}

// Create an express app
const app = express();
const PORT = 1245;

app.use(bodyParser.json());

// Route to get all products
app.get('/list_products', (req, res) => {
  res.json(listProducts);
});

// Route to get a specific product by ID
app.get('/list_products/:itemId', async (req, res) => {
  const { itemId } = req.params;
  const product = getItemById(itemId);

  if (!product) {
    return res.status(404).json({ status: 'Product not found' });
  }

  const currentQuantity = await getCurrentReservedStockById(itemId);
  res.json({
    ...product,
    currentQuantity: currentQuantity !== null ? currentQuantity : product.initialAvailableQuantity
  });
});

// Route to reserve a product
app.get('/reserve_product/:itemId', async (req, res) => {
  const { itemId } = req.params;
  const product = getItemById(itemId);

  if (!product) {
    return res.status(404).json({ status: 'Product not found' });
  }

  const currentQuantity = await getCurrentReservedStockById(itemId);
  const availableStock = currentQuantity !== null ? currentQuantity : product.initialAvailableQuantity;

  if (availableStock <= 0) {
    return res.status(400).json({ status: 'Not enough stock available', itemId });
  }

  reserveStockById(itemId, availableStock - 1);
  res.json({ status: 'Reservation confirmed', itemId });
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
