const express = require('express');
const app = express();
const PORT = process.env.PORT || 3000;

const path = require('path');
const fs = require('fs');

const info = [
  { name: 'widget1', color: 'blue' },
  { name: 'widget2', color: 'green' },
  { name: 'widget3', color: 'black' },
  { name: 'widgetX', color: 'blue' }
];

app.get('/info', (req, res) => {
  res.send(info);
});

app.get('/api', (req, res) => {
  const widgetsPath = path.join(__dirname, 'public', 'widgets.json');

  fs.readFile(widgetsPath, 'utf8', (err, data) => {
    if (err) {
      console.error('Error reading widgets.json:', err);
      res.status(500).send('Internal Server Error');
    } else {
      const widgetsData = JSON.parse(data);
      res.json(widgetsData);
    }
  });
});

app.listen(PORT, (error) => {
  if (!error)
    console.log("Server is Successfully Running, and App is listening on port " + PORT);
  else
    console.log("Error occurred, server can't start", error);
});

