from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_login_error_endpoint():
    response = client.post(url='/login', json={'username': 'montes615', 'password': 'cerro6159'})
    assert response.status_code == 409
    assert response.json()['message'] == 'Wrong username or password'


def test_login_endpoint():
    response = client.post(url='/login', json={'username': 'montes615', 'password': 'cerro61598'})
    assert response.status_code == 200
    assert response.json()['usage'] == 'dogs_breed_api'


def test_register_endpoint():
    response = client.post(url='/register', json={'username': 'montes615', 'password': 'cerro6159', 'usage': 'dogs_breed_api'})
    assert response.status_code == 409
    assert response.json()['message'] == 'The username alredy exists'