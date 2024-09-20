const fs = require('fs').promises;


async function countStudents(path){
    try{
        const data = await fs.readFile(path,
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
        let validStudents = 0;


        students.forEach((student) => {
            const studentField = student[field];
            const studentFirstName = student[firstName];


            if (studentField && studentFirstName){
                fieldStudents[studentField] = fieldStudents[studentField] || [];
                fieldStudents[studentField].push(studentFirstName)
                validStudents++;
            }
        });


        console.log(`Number of students: ${validStudents}`);
        Object.entries(fieldStudents).forEach(([studentField, studentFirstName]) => {
            console.log(`Number of students in ${studentField}: ${studentFirstName.length}. List: ${studentFirstName.join(', ')}`);
        })
    } catch {
        throw new Error('Cannot load the database');
    }
}


module.exports = countStudents;
