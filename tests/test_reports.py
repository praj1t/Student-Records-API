def test_student_report_returns_marks_average_and_grade(client):
    student_response = client.post("/students/", json={"name": "testerman"})
    maths_response = client.post("/subjects/", json={"name": "Maths"})
    english_response = client.post("/subjects/", json={"name": "English"})
    student_id = student_response.json()["id"]
    client.post(
        f"/students/{student_id}/marks",
        json={"subject_id": maths_response.json()["id"], "score": 80},
    )
    client.post(
        f"/students/{student_id}/marks",
        json={"subject_id": english_response.json()["id"], "score": 90},
    )
    response = client.get(f"/students/{student_id}/report")

    assert response.status_code == 200
    assert response.json()["student_id"] == student_id
    assert response.json()["name"] == "testerman"
    assert {mark["subject"]: mark["score"] for mark in response.json()["marks"]} == {
        "Maths": 80,
        "English": 90,
    }
    assert response.json()["average"] == 85
    assert response.json()["letter_grade"] == "B"

def test_student_report_with_no_marks_returns_zero_average_and_f(client):
    student_response = client.post("/students/", json={"name": "testerman"})
    student_id = student_response.json()["id"]
    response = client.get(f"/students/{student_id}/report")

    assert response.status_code == 200
    assert response.json() == {
        "student_id": student_id,
        "name": "testerman",
        "marks": [],
        "average": 0,
        "letter_grade": "F",
    }



def test_missing_student_report_returns_error404(client):
    response = client.get("/students/9999999/report")

    assert response.status_code == 404
    assert response.json() == {"detail": "Student not found"}


def test_student_report_uses_grade_boundaries(client):
    scores_and_grades = [(90, "A"), (80, "B"), (70, "C"), (50, "D"), (49, "F")]
    for number, (score, grade) in enumerate(scores_and_grades):
        student_response = client.post(
            "/students/", json={"name": f"student {number}"}
        )
        subject_response = client.post(
            "/subjects/", json={"name": f"Subject {number}"}
        )
        student_id = student_response.json()["id"]
        client.post(
            f"/students/{student_id}/marks",
            json={"subject_id": subject_response.json()["id"], "score": score},
        )
        response = client.get(f"/students/{student_id}/report")

        assert response.status_code == 200
        assert response.json()["average"] == score
        assert response.json()["letter_grade"] == grade
