from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_login_success():
    r = client.post("/login", json={"email": "user@test.com", "password": "Password1"})
    assert r.status_code == 200


def test_login_wrong_creds_but_valid_format():
    r = client.post("/login", json={"email": "user@test.com", "password": "Password2"})
    assert r.status_code == 401


def test_login_invalid_email_format():
    r = client.post("/login", json={"email": "user@@test..com", "password": "Password1"})
    assert r.status_code == 422


def test_login_invalid_password_symbols_not_allowed():
    r = client.post("/login", json={"email": "user@test.com", "password": "P@ssw0rd123"})
    assert r.status_code == 422


def test_login_invalid_password_no_uppercase():
    r = client.post("/login", json={"email": "user@test.com", "password": "password1"})
    assert r.status_code == 422