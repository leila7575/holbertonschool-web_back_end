const express = require('express');
const app = express();
const path = require('path');
const PORT = process.env.PORT || 1245;

app.get('/', (req, res) => {
    res.setHeader("Content-Type", "text/html");
	res.statuscode = 200;
	res.end('Hello Holberton School!');
});

app.listen(PORT, {});