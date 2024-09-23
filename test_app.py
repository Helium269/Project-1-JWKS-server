
import pytest
import json
import time
from app import app  # Import your Flask app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_jwks(client):
    response = client.get('/.well-known/jwks.json')
    assert response.status_code == 200
    assert 'keys' in json.loads(response.data)

def test_auth_valid(client):
    response = client.post('/auth')
    assert response.status_code == 200
    assert 'token' in json.loads(response.data)

def test_auth_expired(client):
    response = client.post('/auth?expired=true')
    assert response.status_code == 200
    assert 'token' in json.loads(response.data)

def test_no_expired_jwk(client):
    response = client.get('/.well-known/jwks.json')
    keys = json.loads(response.data)['keys']
    assert all(key['expiry'] > time.time() for key in keys)

