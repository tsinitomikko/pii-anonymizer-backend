# PII Anonymizer Backend

This is the backend server for the PII Anonymizer application. It is a Node.js API that uses a Python script to detect and anonymize Personally Identifiable Information (PII) in text.

## Technologies Used

* Node.js (Express)
* Python
* Presidio Analyzer and Anonymizer

## Getting Started

To run the server, you need to have Node.js and Python installed. Follow the steps below based on which PII detection method you want to use.

Option 1: Using Presidio (Recommended)

Install Node.js dependencies:
`npm install`

Install Python dependencies:
`pip install presidio-analyzer presidio-anonymizer`

Ensure the Presidio script is active:
In server.js, make sure the following line is uncommented:
`const pythonProcess = spawn('python', [path.join(__dirname, 'pii_detector_presidio.py'), text]);`
and the Guardrails line is commented out:
`// const pythonProcess = spawn('python', [path.join(__dirname, 'pii_detector_guardrails.py'), text]);`

Start the server:
`node server.js`

Option 2: Using Guardrails

Install Node.js dependencies:
`npm install`

Install Python dependencies:
`pip install guardrails-ai`

Install the PII validator from Guardrails Hub:
`guardrails hub install hub://guardrails/detect_pii`

Ensure the Guardrails script is active:
In server.js, make sure the following line is uncommented:
`const pythonProcess = spawn('python', [path.join(__dirname, 'pii_detector_guardrails.py'), text]);`
and the Presidio line is commented out:
`// const pythonProcess = spawn('python', [path.join(__dirname, 'pii_detector_presidio.py'), text]);`

Start the server:
`node server.js`

API Endpoint
The server will run on http://localhost:3001 and is ready to accept POST requests at the /validate endpoint. The API expects a JSON body with a text field.

JSON
{
  "text": "My email is john.doe@example.com."
}