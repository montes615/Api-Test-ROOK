from fastapi.testclient import TestClient
from app import app

client = TestClient(app)
bearer_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6Im51ZXZvIiwiaWQiOjIsInVzYWdlIjoiZG9nc19icmVlZF9hcGkiLCJleHAiOjE3MzI4NTUzNTB9.5_7qgUAdhRquwuYBNM-KH2yCOPDwIr9i44-x4SCafmg'

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