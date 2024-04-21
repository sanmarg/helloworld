import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_hello_world(client):
    response = client.get('/')
    assert response.data == b'Hello, World!'

def test_hello_world_failure(client):
    response = client.get('/')
    assert response.data != b'Hello, Mars!'
