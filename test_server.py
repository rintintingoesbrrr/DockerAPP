import pytest
import sys
sys.path.insert(0, 'server')
from server import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_hello_endpoint(client):
    response = client.get('/hello')
    assert response.status_code == 200
    assert b'Hello' in response.data

def test_health_endpoint(client):
    response = client.get('/health')
    assert response.status_code == 200
    assert b'App is up and running' in response.data