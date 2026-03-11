const express = require('express');
const mysql = require('mysql2');
const cors = require('cors');
const bodyParser = require('body-parser');

const app = express();
app.use(cors());
app.use(bodyParser.json());

// --- DATABASE CONNECTION ---
const db = mysql.createConnection({
    host: 'localhost',
    user: 'root',      
    password: '8520', // Your MySQL password
    database: 'budgetwise_db'
});

db.connect(err => {
    if (err) console.error('Database Connection Failed:', err);
    else console.log('Connected to MySQL Database');
});

// --- HELPER FUNCTION: PASSWORD VALIDATION ---
function isValidPassword(password) {
    const regex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[\W_]).{8,}$/;
    return regex.test(password);
}

// --- API ENDPOINTS ---

// 1. Sign Up
app.post('/signup', (req, res) => {
    const { name, email, pass, phone, profession } = req.body;
    if (!isValidPassword(pass)) return res.json({ success: false, message: 'Password too weak.' });

    const sql = 'INSERT INTO users (name, email, password, phone, profession) VALUES (?, ?, ?, ?, ?)';
    db.query(sql, [name, email, pass, phone, profession], (err, result) => {
        if (err) return res.json({ success: false, message: 'Email already exists or Database error' });
        res.json({ success: true, message: 'User registered!' });
    });
});

// 2. Login
app.post('/login', (req, res) => {
    const { email, pass } = req.body;
    const sql = 'SELECT * FROM users WHERE email = ? AND password = ?';
    db.query(sql, [email, pass], (err, results) => {
        if (err || results.length === 0) return res.json({ success: false });
        res.json({ success: true, user: results[0] });
    });
});

// 3. Get User Data
app.get('/get-data/:id', (req, res) => {
    const userId = req.params.id;
    db.query('SELECT * FROM users WHERE id = ?', [userId], (err, userResult) => {
        if (err) return res.json({ error: true });
        if (userResult.length === 0) return res.status(404).json({ error: "User not found" });
        
        db.query('SELECT * FROM expenses WHERE user_id = ?', [userId], (err, expResult) => {
            if (err) return res.json({ error: true });
            const userData = userResult[0];
            userData.expenses = expResult;
            res.json(userData);
        });
    });
});

// 4. Update Budget
app.post('/update-budget', (req, res) => {
    const { id, budget } = req.body;
    db.query('UPDATE users SET budget = ? WHERE id = ?', [budget, id], (err) => {
        if (err) return res.json({ success: false });
        res.json({ success: true });
    });
});

// 5. Add Expense
app.post('/add-expense', (req, res) => {
    const { userId, date, amount, note, category } = req.body;
    const sql = 'INSERT INTO expenses (user_id, date, amount, note, category) VALUES (?, ?, ?, ?, ?)';
    db.query(sql, [userId, date, amount, note, category], (err) => {
        if (err) return res.json({ success: false });
        res.json({ success: true });
    });
});

// 6. Update Profile
app.post('/update-profile', (req, res) => {
    const { id, name, email, pass, profession } = req.body;
    if (pass && !isValidPassword(pass)) return res.json({ success: false, message: 'Password too weak.' });

    let sql = 'UPDATE users SET name = ?, email = ?, profession = ? WHERE id = ?';
    let params = [name, email, profession, id];
    
    if (pass) {
        sql = 'UPDATE users SET name = ?, email = ?, profession = ?, password = ? WHERE id = ?';
        params = [name, email, profession, pass, id];
    }
    
    db.query(sql, params, (err) => {
        if (err) return res.json({ success: false });
        res.json({ success: true });
    });
});

// 7. Delete Expense (NEW)
app.delete('/delete-expense/:id', (req, res) => {
    const expId = req.params.id;
    db.query('DELETE FROM expenses WHERE id = ?', [expId], (err) => {
        if (err) return res.json({ success: false });
        res.json({ success: true });
    });
});

// 8. Edit Expense (NEW)
app.post('/edit-expense', (req, res) => {
    const { id, date, amount, note, category } = req.body;
    const sql = 'UPDATE expenses SET date = ?, amount = ?, note = ?, category = ? WHERE id = ?';
    db.query(sql, [date, amount, note, category, id], (err) => {
        if (err) return res.json({ success: false });
        res.json({ success: true });
    });
});

// Start Server
app.listen(3000, () => {
    console.log('Server running on port 3000');
});