from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_job():
    response = client.post("/jobs", json={
        "title": "Software Developer",
        "description": "Develop and maintain software.",
        "location": "Remote",
        "company": "Gorai Tech",
        "salary": 60000
    })
    assert response.status_code == 200
    assert response.json()["id"] == 1

def test_list_jobs():
    response = client.get("/jobs")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
