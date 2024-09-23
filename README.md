# Project 1: JWKS Server

## Overview
This project implements a basic JSON Web Key Set (JWKS) server that generates RSA keys, issues JWTs, and provides endpoints for retrieving the keys and tokens.

## Features
- Generates RSA key pairs.
- Issues valid and expired JWTs.
- Provides JWKS endpoint to retrieve public keys.
- Supports checking for expired keys.

## Technology Stack
- Python
- Flask
- PyJWT
- Cryptography

## Getting Started

### Prerequisites
- Python 3.x
- pip (Python package installer)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Helium269/Project-1-JWKS-server.git
   cd Project-1-JWKS-server

   Set up a virtual environment:

python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows

**Install required packages:**
pip install -r requirements.txt

**Running the Server**
To run the server, use the following command:

python app.py
The server will start at http://127.0.0.1:8080.

**API Endpoints**
GET /.well-known/jwks.json: Retrieves the JWKS containing public keys.
POST /auth: Issues a JWT. Add ?expired=true to get an expired token.

**Testing**
Run the tests using:
pytest test_app.py

**To check test coverage, use:**
pytest --cov=app --cov=auth --cov=jwks


**Acknowledgements**
Flask
PyJWT
Cryptography


Feel free to customize it with any additional details you think are necessary!

