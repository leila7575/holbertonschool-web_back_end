const express = require('express');
const fs = require('fs').promises
const app = express();
const port = 1245;

async function countStudents(path) {
    try {
        const data = await fs.readFile(path, 'utf8');

        if (!data) throw new Error('Cannot load the database');
        const lines = data.trim().split('\n').filter(line => line.length > 0);

        const firstLine = lines.shift().split(',')
        const students = [];
        lines.forEach((line) => {
            students.push(line.split(','));
        })

        const field = firstLine.findIndex(column => column === 'field');
        const firstName = firstLine.findIndex(column => column === 'firstname')

        if (field === -1 || firstName === -1){
            throw new Error('Cannot load the database');
        }

        const fieldStudents = {};
        let validStudents = 0;

        students.forEach((student) => {
            const studentField = student[field];
            const studentFirstName = student[firstName];

            if (studentField && studentFirstName) {
                fieldStudents[studentField] = fieldStudents[studentField] || [];
                fieldStudents[studentField].push(studentFirstName);
                validStudents++;
            }
        });

        let output = `Number of students: ${validStudents}\n`;
        Object.entries(fieldStudents).forEach(([studentField, studentFirstNames]) => {
            output += `Number of students in ${studentField}: ${studentFirstNames.length}. List: ${studentFirstNames.join(', ')}\n`;
        });

        return output.trim();
    } catch (error) {
        console.error(error.message);
        return 'Cannot load the database';
    }
}

app.get('/', (req, res) => {
	res.send('Hello Holberton School!');
});

app.get('/students', async (req, res) => { 
    res.setHeader("Content-Type", "text/plain");
    res.write('This is the list of our students\n');

    const path = process.argv[2];

    if (path) {
        const studentData = await countStudents(path);
        res.end(studentData);
    } else {
        res.end('Cannot load the database');
    }
});

app.listen(port, () => {
console.log(`Server is running on port${port}`);
});

module.exports = app;