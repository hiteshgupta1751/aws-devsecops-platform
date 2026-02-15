import json
from app import app as flask_app

def test_home():
    client = flask_app.test_client()
    resp = client.get("/")
    assert resp.status_code == 200
    data = resp.get_json()
    assert data["status"] == "running"
    assert data["service"] == "devsecops-platform"

def test_analyze():
    client = flask_app.test_client()
    payload = {"numbers": [1, 2, 3, 4]}
    resp = client.post("/analyze", data=json.dumps(payload), content_type="application/json")
    assert resp.status_code == 200
    data = resp.get_json()
    assert data["count"] == 4
    assert data["sum"] == 10
    assert data["average"] == 2.5

