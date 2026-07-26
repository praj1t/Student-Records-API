def test_mark_update_creates_audit_entry(client, created_student, created_subject):
    client.post(
        f"/students/{created_student['id']}/marks",
        json={"subject_id": created_subject["id"], "score": 85},
    )
    client.put(
        f"/students/{created_student['id']}/marks/{created_subject['id']}",
        json={"score": 92, "reason": "Rechecked the paper"},
    )
    response = client.get(f"/students/{created_student['id']}/audit-log")

    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0]["student_id"] == created_student["id"]
    assert response.json()[0]["subject_id"] == created_subject["id"]
    assert response.json()[0]["old_score"] == 85
    assert response.json()[0]["new_score"] == 92
    assert response.json()[0]["reason"] == "Rechecked the paper"
    assert "changed_at" in response.json()[0]

def test_multiple_mark_updates_create_multiple_audit_entries(
    client, created_student, created_subject
):
    client.post(
        f"/students/{created_student['id']}/marks",
        json={"subject_id": created_subject["id"], "score": 85},
    )
    client.put(
        f"/students/{created_student['id']}/marks/{created_subject['id']}",
        json={"score": 90},
    )
    client.put(
        f"/students/{created_student['id']}/marks/{created_subject['id']}",
        json={"score": 95, "reason": "Final review"},
    )
    response = client.get(f"/students/{created_student['id']}/audit-log")

    assert response.status_code == 200
    assert {(entry["old_score"], entry["new_score"], entry["reason"]) for entry in response.json()} == {
        (85, 90, None),
        (90, 95, "Final review"),
    }
def test_audit_log_only_returns_entries_for_requested_student(client):
    first_student = client.post("/students/", json={"name": "testerman"})
    second_student = client.post("/students/", json={"name": "putterman"})
    subject = client.post("/subjects/", json={"name": "Maths"})

    for student, score in [(first_student, 85), (second_student, 70)]:
        student_id = student.json()["id"]
        subject_id = subject.json()["id"]
        client.post(
            f"/students/{student_id}/marks",
            json={"subject_id": subject_id, "score": score},
        )
        client.put(
            f"/students/{student_id}/marks/{subject_id}",
            json={"score": score + 5},
        )

    response = client.get(f"/students/{first_student.json()['id']}/audit-log")

    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0]["student_id"] == first_student.json()["id"]
    assert response.json()[0]["old_score"] == 85
    assert response.json()[0]["new_score"] == 90

def test_missing_student_audit_log_returns_error404(client):
    response = client.get("/students/9999999/audit-log")

    assert response.status_code == 404
    assert response.json() == {"detail": "Student not found"}
