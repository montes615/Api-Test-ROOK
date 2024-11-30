# API-TEST-ROOK

![Python](https://img.shields.io/badge/Python-3.11%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.95.0-green)
![License](https://img.shields.io/github/license/montes615/Api-Test-ROOK?cacheSeconds=0)

Welcome to **API-TEST-ROOK**, a project developed to demonstrate technical skills in integrating third-party APIs, working with databases, and creating unit tests.

## Table of Contents
- [Overview](#overview)
- [Installation](#installation)
- [Running the Project](#running-the-project)
- [Usage](#usage)
- [Running Tests](#running-tests)
- [Technologies Used](#technologies-used)
- [License](#license)

## Overview
**API-TEST-ROOK** is a FastAPI-based application that includes features such as user authentication, token management, and rate limiting. The project also integrates MySQL for data persistence and provides comprehensive API documentation through Swagger.

## Installation
Follow these steps to set up the project locally (Ensure Python 3.11 or higher is installed):

1. **Clone the repository**:
   ```bash
    git clone https://github.com/montes615/Api-Test-ROOK.git
    cd Api-Test-ROOK

2. **Create and activate a virtual environment**:
   ```bash
    Linux/macOS:
    python3 -m venv venv
    source venv/bin/activate

    Windows:
    python -m venv venv
    venv\Scripts\activate

3. **Install the dependencies**:
    ```bash
    Linux/macOS:
    pip3 install -r requirements.txt
    
    Windows:
    pip install -r requirements.txt


## Running the project

1.  **Production Mode**:
    ```bash|shell|cmd
    Run the application using Uvicorn:
    uvicorn app.main:app

2.  **Developer Mode**:
    ```bash|shell|cmd
    For development mode with live reload:
    uvicorn app.main:app --reload


## Usage

1.  **Docs**;
    Open your browser and go to http://localhost:8000/docs to access the Swagger-generated API documentation.

2.  **Authentication**;
    Use the /login or /register endpoints to create or log in to a user account.
    Follow the provided request schemas.

3. **Access Protected Endpoints**:
    After obtaining an access token (valid for 60 minutes), include it in your requests with Authorization button in the UI (only add the token)
    or adding this in the authorization headers if your are using postman or other http client:
    Headers: { "Authorization": "Bearer {{Token}}" }


## Running Tests
Run the following command in the project root to execute the unit tests: pytest
Note: For the protected endpoints is necesary add a valid token


## Technologies Used
    Python: Core programming language.
    MySQL: Database management.
    FastAPI: Web framework for building APIs.
    SlowAPI: Rate limiting middleware.
    Swagger: API documentation integration.
    Pytest: Unit testing framework.

## License
This proyect is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details
