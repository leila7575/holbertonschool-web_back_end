const fs = require('fs');


function countStudents(path){
    try{
        const data = fs.readFileSync(path,
            { encoding:'utf8', });


        if (!data) throw new Error('Cannot load the database')
        const lines = data.split('\n')


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


        students.forEach((student) => {
            const studentField = student[field];
            const studentFirstName = student[firstName];


            if (studentField && studentFirstName){
                fieldStudents[studentField] = fieldStudents[studentField] || [];
                fieldStudents[studentField].push(studentFirstName)
            }
        });


        console.log(`Number of students: ${students.length}`);
        Object.entries(fieldStudents).forEach(([studentField, studentFirstName]) => {
            console.log(`Number of students in ${studentField}: ${studentFirstName.length}. List: ${studentFirstName.join(', ')}`);
        })
    } catch {
        throw new Error('Cannot load the database');
    }
}


module.exports = countStudents;

