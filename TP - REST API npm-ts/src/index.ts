// src/index.ts

import express, { Request, Response } from 'express';

const app = express();
const PORT = 3000;

// Endpoint "Hello World".
app.get('/hello', (req: Request, res: Response) => {
  console.log('/hello requested');
  res.send('Hello World!');
});

// Start the server.
app.listen(PORT, () => {
  console.log(`Server started on http://localhost:${PORT}`);
});
