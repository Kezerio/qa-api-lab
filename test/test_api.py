from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health_ok():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}


def test_login_success():
    r = client.post("/login", json={"email": "user@test.com", "password": "P@ssw0rd123"})
    assert r.status_code == 200
    assert r.json()["ok"] is True
    assert r.json()["message"] == "dashboard"


def test_login_wrong_password():
    r = client.post("/login", json={"email": "user@test.com", "password": "wrong"})
    assert r.status_code == 200
    assert r.json()["ok"] is False
    assert r.json()["message"] == "Invalid email or password"


def test_login_empty_password():
    r = client.post("/login", json={"email": "user@test.com", "password": "   "})
    assert r.status_code == 200
    assert r.json()["ok"] is False
    assert r.json()["message"] == "Password is required"


def test_login_invalid_email_format_422():
    r = client.post("/login", json={"email": "user@@test..com", "password": "P@ssw0rd123"})
    assert r.status_code == 422