const express = require('express');
const bodyParser = require('body-parser');
const { spawn } = require('child_process');
const path = require('path');
const cors = require('cors');

const app = express();
const port = 3001;

app.use(cors());
app.use(bodyParser.json());

app.post('/validate', (req, res) => {
  const { text } = req.body;

  if (!text) {
    return res.status(400).json({ error: 'Text input is required.' });
  }

  // pii_detector_presidio
  const pythonProcess = spawn('python', [path.join(__dirname, 'pii_detector_presidio.py'), text]);
  // pii_detector_guardrails
  //const pythonProcess = spawn('python', [path.join(__dirname, 'pii_detector_guardrails.py'), text]);

  let pythonStdout = '';
  let pythonStderr = '';

  pythonProcess.stdout.on('data', (data) => {
    pythonStdout += data.toString();
  });

  pythonProcess.stderr.on('data', (data) => {
    pythonStderr += data.toString();
    console.error(`Python stderr: ${data.toString()}`);
  });

  pythonProcess.on('close', (code) => {
    if (code === 0) {
      try {
        const result = JSON.parse(pythonStdout);
        res.json(result);
      } catch (e) {
        console.error('Failed to parse JSON from Python script:', e);
        res.status(500).json({ error: 'Internal server error: Failed to parse Python output.', details: pythonStdout });
      }
    } else {
      console.error(`Python script failed with code ${code}.`);
      console.error(`Python stderr: ${pythonStderr}`);
      res.status(500).json({ error: `Python script failed with code ${code}.`, details: pythonStderr });
    }
  });
});

app.listen(port, () => {
  console.log(`Backend server listening at http://localhost:${port}`);
});