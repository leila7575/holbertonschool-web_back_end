const express = require('express');

const app = express();
const port = 1245;
const host = '0.0.0.0';

app.get('/', (req, res) => {
	res.send('Hello Holberton School!');
});

app.listen(port, host, () => {
	console.log(`Server listening at http://${host}:${port}`);
});

module.exports = app;
