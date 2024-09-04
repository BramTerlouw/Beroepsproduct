const express = require('express');
const { Client } = require('pg');
const cors = require('cors');

const app = express();
const port = 3000;

const client = new Client({
    user: 'dev',
    host: '<<route>>',
    database: 'incidents',
    password: 'password',
    port: 5432,
});

app.use(cors());
app.use(express.json());

client.connect()
    .then(() => console.log('Connected to PostgreSQL'))
    .catch(err => console.error('Connection error', err.stack));

app.get('/api/incidents', async (req, res) => {
    try {
        const result = await client.query('SELECT * FROM fracture_incidents');
        res.json(result.rows);
    } catch (err) {
        console.error('Error executing query', err.stack);
        res.status(500).json({ error: 'Internal Server Error' });
    }
});

app.listen(port, () => {
    console.log(`Server running on http://localhost:${port}`);
});
