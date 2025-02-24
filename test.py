import requests
import pytest

URL = "https://fakestoreapi.com"

def test_get_all_products():
    response = requests.get(f"{URL}/products")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_single_product():
    response = requests.get(f"{URL}/products/1")
    assert response.status_code == 200
    data = response.json()
    assert "id" in data and data["id"] == 1
    assert "title" in data

def test_create_product():
    new_product = {
        "title": "Test Product",
        "price": 99.99,
        "description": "Test description",
        "image": "https://i.pravatar.cc",
        "category": "test-category"
    }
    response = requests.post(f"{URL}/products", json=new_product)
    assert response.status_code == 200 or response.status_code == 201
    data = response.json()
    assert "id" in data

def test_update_product():
    updated_product = {
        "title": "Updated Test Product",
        "price": 79.99,
        "description": "Updated description",
        "image": "https://i.pravatar.cc",
        "category": "updated-category"
    }
    response = requests.put(f"{URL}/products/1", json=updated_product)
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Updated Test Product"
    assert data["price"] == 79.99

def test_delete_product():
    response = requests.delete(f"{URL}/products/1")
    assert response.status_code == 200
    data = response.json()
    assert "id" in data and data["id"] == 1

def test_get_existent_user():
    response = requests.get(f"{URL}/users/9999")
    assert response.status_code == 200
