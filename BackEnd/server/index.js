const express = require('express');
const mysql = require('mysql2');
const app = express();
const cors = require('cors');

app.use(cors());
app.use(express.json());

const db = mysql.createConnection({
    user : 'root',
    host : 'localhost',
    password : '1903',
    database : 'Medical_Store',
});

app.post('/SignIn', (req, res) =>{
    const {id, password} = req.body;

    db.query('SELECT * FROM employee_credentials WHERE employee_login_id = ? AND employee_login_password = ?', 
    [Number(id), password], 
    (err, result) => {
        if(err){
            console.log(err);
        } else{
            res.json({id: result[0]});
        }
    });
})

app.listen(3001, () => {
    console.log("Server running on port 3001")
});