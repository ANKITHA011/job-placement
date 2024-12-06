from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

# Test data to be reused across multiple tests
test_job_data = {
    "title": "Software Developer",
    "description": "Develop and maintain software.",
    "location": "Remote",
    "company": "Intel",
    "salary": 60000
}

def test_create_job():
    """Test the creation of a job post."""
    response = client.post("/jobs", json=test_job_data)
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert data["title"] == test_job_data["title"]
    assert data["description"] == test_job_data["description"]

def test_list_jobs():
    """Test retrieving the list of all job posts."""
    response = client.get("/jobs")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0  # Ensure at least one job is present

def test_get_job_by_id():
    """Test retrieving a job post by its ID."""
    # Create a new job to ensure it exists
    create_response = client.post("/jobs", json=test_job_data)
    job_id = create_response.json()["id"]
    
    # Retrieve the job post by its ID
    response = client.get(f"/jobs/{job_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == job_id
    assert data["title"] == test_job_data["title"]

def test_delete_job():
    """Test deleting a job post by its ID."""
    # Create a new job to ensure it exists
    create_response = client.post("/jobs", json=test_job_data)
    job_id = create_response.json()["id"]
    
    # Delete the job post
    delete_response = client.delete(f"/jobs/{job_id}")
    assert delete_response.status_code == 200
    assert delete_response.json() == {"message": "Job post deleted successfully"}
    
    # Verify the job is no longer retrievable
    get_response = client.get(f"/jobs/{job_id}")
    assert get_response.status_code == 404
    assert get_response.json() == {"detail": "Job post not found"}

