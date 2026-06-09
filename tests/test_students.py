from fastapi.testclient import TestClient
from app.main import app
from app.database import open_file,write_file

client = TestClient(app)

def test_healthcheck_returns_success():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "message": "Student records api is currently running"
    }

def test_students_returns_all_student_data():
    response = client.get("/students")
    assert response.status_code == 200
    assert response.json() == open_file()

def test_get_students_with_id_returns_student():
    response = client.post("/students", json={"name": "testerman", "marks": {"English": 85, "Maths": 92, "Physics": 78, "Programming": 95}})
    student_id = response.json()["id"]
    get_response = client.get(f"/students/{student_id}")
    assert get_response.status_code == 200
    assert get_response.json() == response.json()

def test_get_students_with_invalid_id_returns_error404():
    response = client.get("/students/9999999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Student was not found"}

def test_delete_students_with_id_deletes_student():
    response = client.post("/students", json={"name": "testerman", "marks": {"English": 85, "Maths": 92, "Physics": 78, "Programming": 95}})
    student_id = response.json()["id"]
    deletion = client.delete(f"/students/{student_id}")
    assert deletion.status_code == 200
    assert deletion.json() == {"message": "Student was successfully deleted"}
    get_response = client.get(f"/students/{student_id}")
    assert get_response.status_code == 404

def test_put_updates_student_data():
    response = client.post("/students", json={"name": "testerman", "marks": {"English": 85, "Maths": 92, "Physics": 78, "Programming": 95}})
    student_id = response.json()["id"]
    updated_response = client.put(f"/students/{student_id}", json={"name": "putterman", "marks": {"English": 85, "Maths": 92, "Physics": 78, "Programming": 95}})
    get_response = client.get(f"/students/{student_id}")
    assert updated_response.status_code == 200
    assert get_response.status_code == 200
    assert get_response.json() == updated_response.json()

def test_report_endpoint_returns_reportcard():
    response = client.post("/students", json={"name": "testerman", "marks": {"English": 100,"Maths": 100,"Physics": 100,"Programming": 100}})
    student_id = response.json()["id"]
    report = client.get(f"/students/{student_id}/report")
    assert report.status_code == 200
    assert report.json()["average"] == 100
    assert report.json()["grade"] == "A"

def test_post_student_emptyname_returns_error422():
    response = client.post("/students",json={"name": "","marks": {"English": 85,"Maths": 92,"Physics": 78,"Programming": 95}})
    assert response.status_code == 422