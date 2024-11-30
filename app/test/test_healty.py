from fastapi.testclient import TestClient
from app import app

client = TestClient(app)
bearer_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6Im1vbnRlczYxNSIsImlkIjoxLCJ1c2FnZSI6ImRvZ3NfYnJlZWRfYXBpIiwiZXhwIjoxNzM4MTE3MjkyfQ.1caGhdRBv6Uq4n7UpbXqy-lpvXKWB2tAWhNBDcTubks'

def test_healty_endpoint():
    '''Tests if the /healty endpoint function correctly and the responses of breed_api and db are okay'''
    response = client.get(url='/healty', headers={"Authorization": f"Bearer {bearer_token}"})
    assert response.status_code == 200
    data = response.json()
    
    assert 'db' in data and 'breed_api' in data
    assert data['db']['status'] == 'ok' and data['breed_api']['status'] == 'ok'
    assert data['db']['message'] == 'All fine!' and data['breed_api']['message'] == 'All fine!'