# tests/test_products.py

import pytest
from fastapi.testclient import TestClient
from main import app, Base, engine

client = TestClient(app)

@pytest.fixture(autouse=True)
def setup_db():
    # Clean up and recreate the database before each test
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

def test_get_empty_products_list():
    response = client.get("/products/")
    assert response.status_code == 200
    assert response.json() == []

def test_create_product():
    payload = {
        "name": "Test Product",
        "description": "A test product",
        "price": 9.99,
        "quantity": 5
    }
    response = client.post("/add/product/", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert data["name"] == payload["name"]
    assert data["description"] == payload["description"]
    assert data["price"] == payload["price"]
    assert data["quantity"] == payload["quantity"]

def test_get_product_by_id():
    payload = {
        "name": "Test Product",
        "description": "A test product",
        "price": 9.99,
        "quantity": 5
    }
    client.post("/add/product/", json=payload)
    response = client.get("/products/1")
    assert response.status_code == 200
    data = response.json()
    assert data["product"]["id"] == 1
    assert data["product"]["name"] == payload["name"]

def test_update_product():
    payload = {
        "name": "Original Product",
        "description": "Original description",
        "price": 1.0,
        "quantity": 1
    }
    client.post("/add/product/", json=payload)
    update_payload = {
        "name": "Updated Product",
        "description": "Updated description",
        "price": 2.0,
        "quantity": 2
    }
    response = client.put("/products/1", json=update_payload)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == update_payload["name"]
    assert data["price"] == update_payload["price"]
    assert data["quantity"] == update_payload["quantity"]

def test_delete_product():
    payload = {
        "name": "Delete Me",
        "description": "To be deleted",
        "price": 5.0,
        "quantity": 1
    }
    client.post("/add/product/", json=payload)
    response = client.delete("/products/1")
    assert response.status_code == 200
    message = response.json().get("message", "")
    assert "Deleted product 1" in message
    response2 = client.get("/products/1")
    assert response2.status_code == 404

def test_nonexistent_product_returns_404():
    response = client.get("/products/999")
    assert response.status_code == 404

def test_invalid_price_returns_400():
    payload = {
        "name": "Bad Product",
        "description": "Invalid price",
        "price": -1,
        "quantity": 1
    }
    response = client.post("/add/product/", json=payload)
    assert response.status_code == 400

