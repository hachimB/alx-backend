import express from 'express';
import { createClient } from 'redis';
import redis from 'redis';
import util from 'util';

const listProducts = [
  {Id: 1, name: 'Suitcase 250', price: 50, stock: 4},
  {Id: 2, name: 'Suitcase 450', price: 100, stock: 10},
  {Id: 3, name: 'Suitcase 650', price: 350, stock: 2},
  {Id: 4, name: 'Suitcase 1050', price: 550, stock: 5},
]

const getItemById = (id) => {
  return listProducts.find((product) => product.Id === id );
}

const app = express();
const port = 1245;
const host = '127.0.0.1';


app.get('/list_products', (req, res) => {
  const products = listProducts.map((product) => ({
    itemId: product.Id,
    itemName: product.name,
    price: product.price,
    initialAvailableQuantity: product.stock,
  }));
  res.send(products);
});


app.listen(port, host, () => {
  console.log(`The server is running on port ${port}.`);
})



const client = createClient();



const reserveStockById = (itemId, stock) => {
  client.set(`item.${itemId}`, stock, redis.print);
}



const getAsync = util.promisify(client.get).bind(client);

const getCurrentReservedStockById = async (itemId) => {
  try {
    const res = await getAsync(`item.${itemId}`);
    return res;
  } catch (err) {
    console.error(err);
  }
}

app.get('/list_products/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId);
  const product = listProducts.find(product => product.Id === itemId);

  if (!product) {
    return res.status(404).json({ status: 'Product not found' });
  }

  try {
    const stock = await getCurrentReservedStockById(itemId);
    const response = {
      itemId: product.Id,
      itemName: product.name,
      price: product.price,
      initialAvailableQuantity: product.stock,
      currentQuantity: product.stock
    };
    res.json(response);
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: 'Failed to get stock' });
  }
});


app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId);
  const product = listProducts.find(product => product.Id === itemId);

  if (!product) {
    return res.status(404).json({ status: 'Product not found' });
  }

  try {
    const stock = await getCurrentReservedStockById(itemId);
    if (stock < 1) {
      return res.status(200).json({ status: 'Not enough stock available', itemId: itemId });
    }

    await reserveStockById(itemId, stock - 1);
    return res.status(200).json({ status: 'Reservation confirmed', itemId: itemId });
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: 'Failed to reserve product' });
  }
});