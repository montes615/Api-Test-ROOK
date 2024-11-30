from fastapi.testclient import TestClient
from app import app

client = TestClient(app)
bearer_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6Im51ZXZvIiwiaWQiOjIsInVzYWdlIjoiZG9nc19icmVlZF9hcGkiLCJleHAiOjE3MzI4NTUzNTB9.5_7qgUAdhRquwuYBNM-KH2yCOPDwIr9i44-x4SCafmg'

def test_healty_endpoint():
    '''Tests if the /healty endpoint function correctly and the responses of breed_api and db are okay'''
    response = client.get(url='/healty', headers={"Authorization": f"Bearer {bearer_token}"})
    assert response.status_code == 200
    data = response.json()
    
    assert 'db' in data and 'breed_api' in data
    assert data['db']['status'] == 'ok' and data['breed_api']['status'] == 'ok'
    assert data['db']['message'] == 'All fine!' and data['breed_api']['message'] == 'All fine!'