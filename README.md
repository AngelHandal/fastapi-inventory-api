# fastapi-inventory-api

A simple Inventory Management REST API built with FastAPI, SQLAlchemy & SQLite (with Pytest tests).

---

## Table of Contents

- [Features](#features)  
- [Tech Stack](#tech-stack)  
- [Getting Started](#getting-started)  
  - [Prerequisites](#prerequisites)  
  - [Installation](#installation)  
  - [Running the Server](#running-the-server)  
- [Usage](#usage)  
  - [List Products](#list-products)  
  - [Create a Product](#create-a-product)  
  - [Get Product by ID](#get-product-by-id)  
  - [Update a Product](#update-a-product)  
  - [Delete a Product](#delete-a-product)  
- [Running Tests](#running-tests)  
- [License](#license)

---

## Features

- CRUD endpoints for **Products**  
- Data validation with **Pydantic**  
- SQLite persistence via **SQLAlchemy** ORM  
- Automatic docs at `/docs` and `/redoc`  
- Unit & integration tests with **Pytest** & **TestClient**

---

## Tech Stack

- **Python 3.13**  
- **FastAPI**  
- **Uvicorn** (ASGI server)  
- **SQLAlchemy** (ORM)  
- **SQLite** (database)  
- **Pydantic** (data validation)  
- **Pytest** & **httpx** (testing)

---

## Getting Started

### Prerequisites

- Python 3.7+  
- Git

### Installation

```bash
git clone https://github.com/AngelHandal/fastapi-inventory-api.git
cd fastapi-inventory-api

python -m venv env
source env/bin/activate       # Mac/Linux
.\env\Scripts\activate.ps1    # Windows PowerShell

pip install -r requirements.txt
```

### Running the Server

```bash
uvicorn main:app --reload
```

## Usage

### List Products

```bash
curl -X GET http://127.0.0.1:8000/products/
```

### Create a Product

```bash
curl -X POST http://127.0.0.1:8000/add/product/ \
  -H "Content-Type: application/json" \
  -d '{ "name": "New Widget", "description": "A shiny new widget", "price": 19.99, "quantity": 10 }'
```

### Get Product by ID

```bash
curl -X GET http://127.0.0.1:8000/products/1
```

### Update a Product

```bash
curl -X PUT http://127.0.0.1:8000/products/1 \
  -H "Content-Type: application/json" \
  -d '{ "name": "Updated Widget", "description": "Now even shinier", "price": 24.99, "quantity": 5 }'
```

### Delete a Product

```bash
curl -X DELETE http://127.0.0.1:8000/products/1
```

## Running Tests

```bash
pytest -q
```

## License

This project is licensed under the MIT License.
