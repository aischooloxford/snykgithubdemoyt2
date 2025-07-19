import json
from app import app

def test_home():
    response = app.test_client().get('/')
    assert response.status_code == 200
    assert b'Welcome to the Dummy API!' in response.data

def test_list_users():
    response = app.test_client().get('/users')
    assert response.status_code == 200
    data = response.get_json()
    assert "alice" in data
    assert "bob" in data

def test_get_user_success():
    response = app.test_client().get('/users/alice')
    assert response.status_code == 200
    assert response.get_json() == {"alice": {"email": "alice@example.com"}}

def test_get_user_not_found():
    response = app.test_client().get('/users/charlie')
    assert response.status_code == 404

def test_create_user_success():
    payload = {"username": "charlie", "email": "charlie@xyz.com"}
    response = app.test_client().post(
        '/users',
        data=json.dumps(payload),
        content_type='application/json'
    )
    assert response.status_code == 201
    data = response.get_json()
    assert "charlie" in data
    assert data["charlie"]["email"] == "charlie@xyz.com"

def test_create_user_bad_request():
    response = app.test_client().post('/users', data="{}", content_type='application/json')
    assert response.status_code == 400
