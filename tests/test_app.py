import pytest
from app import app as flask_app

@pytest.fixture
def app():
    flask_app.config.update({
        "TESTING": True,
    })
    yield flask_app

@pytest.fixture
def client(app):
    return app.test_client()

def test_index(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"A Toy Browser Fingerprinting Tool" in response.data

def test_fingerprint(client):
    response = client.post("/fingerprint")
    assert response.status_code == 200
    assert b"A Toy Browser Fingerprinting Tool" in response.data
