from fastapi.testclient import TestClient
from app import app

client = TestClient(app)
bearer_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6Im1vbnRlczYxNSIsImlkIjoxLCJ1c2FnZSI6ImRvZ3NfYnJlZWRfYXBpIiwiZXhwIjoxNzM4MTE3MjkyfQ.1caGhdRBv6Uq4n7UpbXqy-lpvXKWB2tAWhNBDcTubks'

def test_breed_endpoint():
    '''Tests the /dog/breed/{breed_name} endpoint if the Breed CEO api are available'''
    response = client.get(url='/dog/breed/hound', headers={"Authorization": f"Bearer {bearer_token}"})
    assert response.status_code == 200
    assert response.json()['breed_name'] == 'hound'


def test_stats_endpoint():
    '''Tests if the /stats endpoint funcion correctly and gets only 10 or less records'''
    response = client.get(url='/stats', headers={"Authorization": f"Bearer {bearer_token}"})
    assert response.status_code == 200
    
    data = response.json()
    assert 'top_breeds' in data
    assert len(data['top_breeds']) <= 10