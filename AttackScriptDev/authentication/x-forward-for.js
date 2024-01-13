const express = require('express');
const app = express();

app.get('/', (req, res) => {
  req.headers['x-forwarded-for']=500
  const clientIp = req.headers['x-forwarded-for'] || req.connection.remoteAddress;
  res.send(`Client IP: ${clientIp}`)
});

app.listen(3000, () => {
  console.log('Server listening on port 3000');
});