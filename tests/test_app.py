import pytest
from werkzeug.test import Client

from app import application


@pytest.fixture
def client():
    return Client(application)


def test_default(client):
    response = client.get('/')
    assert response.status == '200 OK'
    assert response.data == b'Hello, World!'

def test_name(client):
    response = client.get('/?name=Test')
    assert response.status == '200 OK'
    assert response.data == b'Hello, Test!'
