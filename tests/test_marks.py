def test_create_mark_returns_mark_data(client, created_student, created_subject):
    response = client.post(
        f"/students/{created_student['id']}/marks",
        json={"subject_id": created_subject["id"], "score": 85},
    )

    assert response.status_code == 200
    assert response.json()["id"] == 1
    assert response.json()["student_id"] == created_student["id"]
    assert response.json()["subject_id"] == created_subject["id"]
    assert response.json()["score"] == 85
    assert "created_at" in response.json()
    assert "updated_at" in response.json()

def test_update_mark_changes_score(client, created_student, created_subject):
    client.post(
        f"/students/{created_student['id']}/marks",
        json={"subject_id": created_subject["id"], "score": 85},
    )
    response = client.put(
        f"/students/{created_student['id']}/marks/{created_subject['id']}",
        json={"score": 92, "reason": "Rechecked the paper"},
    )

    assert response.status_code == 200
    assert response.json()["student_id"] == created_student["id"]
    assert response.json()["subject_id"] == created_subject["id"]
    assert response.json()["score"] == 92

def test_create_duplicate_mark_returns_error409(client, created_student, created_subject):
    client.post(
        f"/students/{created_student['id']}/marks",
        json={"subject_id": created_subject["id"], "score": 85},
    )
    response = client.post(
        f"/students/{created_student['id']}/marks",
        json={"subject_id": created_subject["id"], "score": 92},
    )

    assert response.status_code == 409
    assert response.json() == {
        "detail": "Mark already exists for this student and subject"
    }

def test_create_mark_for_missing_student_returns_error404(client, created_subject):
    response = client.post(
        "/students/9999999/marks",
        json={"subject_id": created_subject["id"], "score": 85},
    )

    assert response.status_code == 404
    assert response.json() == {"detail": "Student not found"}

def test_create_mark_for_missing_subject_returns_error404(client, created_student):
    response = client.post(
        f"/students/{created_student['id']}/marks",
        json={"subject_id": 9999999, "score": 85},
    )

    assert response.status_code == 404
    assert response.json() == {"detail": "Subject not found"}

def test_create_mark_with_score_above_100_returns_error422(
    client, created_student, created_subject
):
    response = client.post(
        f"/students/{created_student['id']}/marks",
        json={"subject_id": created_subject["id"], "score": 101},
    )

    assert response.status_code == 422
    assert response.json()["detail"][0]["loc"] == ["body", "score"]
    assert response.json()["detail"][0]["msg"] == "Value error, Mark entered should be between 0-100!"

def test_update_mark_with_negative_score_returns_error422(
    client, created_student, created_subject
):
    response = client.put(
        f"/students/{created_student['id']}/marks/{created_subject['id']}",
        json={"score": -1},
    )

    assert response.status_code == 422
    assert response.json()["detail"][0]["loc"] == ["body", "score"]
    assert response.json()["detail"][0]["msg"] == "Value error, Mark entered should be between 0-100!"
