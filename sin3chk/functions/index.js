const functions = require('firebase-functions');
const admin = require('firebase-admin');
const express = require('express');
const bodyParser = require('body-parser');
const path = require('path');

admin.initializeApp();
const db = admin.database();

const app = express();
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// Flask 서버 실행
const { spawn } = require('child_process');
const pythonProcess = spawn('python', [path.join(__dirname, 'main.py')]);

app.all('*', (req, res) => {
    res.send('Python Flask server is running');
});

exports.api = functions.https.onRequest(app);
