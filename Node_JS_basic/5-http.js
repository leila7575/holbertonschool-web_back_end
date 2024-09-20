const http = require('http');
const url = require('url');
const countStudents = require('./3-read_file_async');

const app = http.createServer((req, res) => {
    const parsedUrl = url.parse(req.url, true);
    res.setHeader('Content-Type', 'text/plain');

    if (parsedUrl.pathname === '/') {
        res.statusCode = 200;
        res.end('Hello Holberton School!');
    } else if (parsedUrl.pathname === '/students') {
    
        res.statusCode = 200;
        res.write('This is the list of our students\n');
        
        const databaseFile = process.argv[2];

        countStudents(databaseFile)
            .then((output) => {
                res.write(`${output}\n`);
                res.end();
            })
            .catch((err) => {
                res.write(err.message);
                res.end();
            });
    } else {
        res.statusCode = 404;
        res.end('Not Found');
    }
});

app.listen(1245, () => {
    console.log('Server running at http://localhost:1245/');
});

module.exports = app;