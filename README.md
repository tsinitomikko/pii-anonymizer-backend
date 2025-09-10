# PII Anonymizer Backend

This is the backend server for the PII Anonymizer application. It is a Node.js API that uses a Python script to detect and anonymize Personally Identifiable Information (PII) in text.

## Technologies Used

* Node.js (Express)
* Python
* Presidio Analyzer and Anonymizer

## Getting Started

To run the server, you need to have Node.js and Python installed.

1.  Install Node.js dependencies:
    `npm install`
2.  Install Python dependencies:
    `pip install presidio-analyzer presidio-anonymizer`
3.  Start the server:
    `node server.js`

The server will run on `http://localhost:3001` and is ready to accept API requests.