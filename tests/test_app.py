from werkzeug.test import Client

from app import application


def test_application():
    client = Client(application)
    response = client.get('/')
    assert response.status == '200 OK'
    assert response.data == b'Hello, World!'
