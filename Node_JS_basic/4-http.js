const http = require("http");

const host = 'localhost';
const port = 1245;

const requestListener = function (req, res) {
	res.setHeader("Content-Type", "text/plain");
	res.statuscode = 200;
	res.end('Hello Holberton School!');
};

const app = http.createServer(requestListener);
app.listen(port, host);

module.exports = app;