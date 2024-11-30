from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_login_error_endpoint():
    '''Test the login endpoint if the user data are wrong'''
    response = client.post(url='/login', json={'username': 'montes615', 'password': 'cerro6159'})
    assert response.status_code == 409
    assert response.json()['message'] == 'Wrong username or password'


def test_login_endpoint():
    '''Test the login endpoint if the user data are correct'''
    response = client.post(url='/login', json={'username': 'montes615', 'password': 'cerro61598'})
    assert response.status_code == 200
    assert response.json()['usage'] == 'dogs_breed_api'


def test_register_endpoint():
    '''Test the register endpoint if the alredy exists'''
    response = client.post(url='/register', json={'username': 'montes615', 'password': 'cerro6159', 'usage': 'dogs_breed_api'})
    assert response.status_code == 409
    assert response.json()['message'] == 'The username alredy exists'