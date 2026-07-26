def test_create_student_returns_student_data(client):
    response = client.post("/students/", json={"name": "testerman"})

    assert response.status_code == 200
    assert response.json()["id"] == 1
    assert response.json()["name"] == "testerman"
    assert "created_at" in response.json()
    assert "updated_at" in response.json()


def test_students_returns_all_student_data(client):
    first_response = client.post("/students/", json={"name": "testerman"})
    second_response = client.post("/students/", json={"name": "putterman"})
    response = client.get("/students/")

    assert response.status_code == 200
    assert response.json() == [first_response.json(), second_response.json()]


def test_get_student_with_id_returns_student(client):
    created_student = client.post("/students/", json={"name": "testerman"})
    student_id = created_student.json()["id"]
    response = client.get(f"/students/{student_id}")

    assert response.status_code == 200
    assert response.json() == created_student.json()


def test_update_student_changes_student_data(client):
    created_student = client.post("/students/", json={"name": "testerman"})
    student_id = created_student.json()["id"]
    response = client.put(f"/students/{student_id}", json={"name": "putterman"})
    get_response = client.get(f"/students/{student_id}")

    assert response.status_code == 200
    assert response.json()["id"] == student_id
    assert response.json()["name"] == "putterman"
    assert get_response.status_code == 200
    assert get_response.json() == response.json()


def test_delete_student_deletes_student(client):
    created_student = client.post("/students/", json={"name": "testerman"})
    student_id = created_student.json()["id"]
    response = client.delete(f"/students/{student_id}")
    get_response = client.get(f"/students/{student_id}")

    assert response.status_code == 200
    assert response.json() == {"message": "Student deleted successfully"}
    assert get_response.status_code == 404
    assert get_response.json() == {"detail": "Student not found"}


def test_get_missing_student_returns_error404(client):
    response = client.get("/students/9999999")

    assert response.status_code == 404
    assert response.json() == {"detail": "Student not found"}


def test_update_missing_student_returns_error404(client):
    response = client.put("/students/9999999", json={"name": "putterman"})

    assert response.status_code == 404
    assert response.json() == {"detail": "Student not found"}


def test_delete_missing_student_returns_error404(client):
    response = client.delete("/students/9999999")

    assert response.status_code == 404
    assert response.json() == {"detail": "Student not found"}


def test_create_student_strips_name_whitespace(client):
    response = client.post("/students/", json={"name": "  testerman  "})

    assert response.status_code == 200
    assert response.json()["name"] == "testerman"


def test_create_student_with_empty_name_returns_error422(client):
    response = client.post("/students/", json={"name": "   "})

    assert response.status_code == 422
    assert response.json()["detail"][0]["loc"] == ["body", "name"]
    assert response.json()["detail"][0]["msg"] == "Value error, Name cannot be empty"


def test_create_student_without_name_returns_error422(client):
    response = client.post("/students/", json={})

    assert response.status_code == 422
    assert response.json()["detail"][0]["loc"] == ["body", "name"]
    assert response.json()["detail"][0]["msg"] == "Field required"
