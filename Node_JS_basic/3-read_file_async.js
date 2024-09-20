const fs = require('fs').promises;

function countStudents(path) {
    return fs.readFile(path, 'utf-8')
        .then((data) => {
            const lines = data.trim().split('\n');
            if (lines.length === 0) {
                throw new Error('Cannot load the database');
            }

            const students = [];
            const fields = {};

            lines.slice(1).forEach((line) => {
                const parts = line.split(',');
                if (parts.length === 4 && parts.every((part) => part.trim().length > 0)) {
                    const student = {
                        firstname: parts[0],
                        lastname: parts[1],
                        age: parts[2],
                        field: parts[3]
                    };
                    students.push(student);

                    if (!fields[student.field]) {
                        fields[student.field] = [];
                    }
                    fields[student.field].push(student.firstname);
                }
            });

            console.log(`Number of students: ${students.length}`);

            for (const field in fields) {
                const studentList = fields[field].join(', ');
                console.log(`Number of students in ${field}: ${fields[field].length}. List: ${studentList}`);
            }
        })
        .catch (() => {
            throw new Error('Cannot load the database');
        });
}

module.exports = countStudents;
