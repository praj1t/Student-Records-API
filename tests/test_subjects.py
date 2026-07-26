def test_create_subject_returns_subject_data(client):
    response = client.post("/subjects/", json={"name": "Maths"})

    assert response.status_code == 200
    assert response.json()["id"] == 1
    assert response.json()["name"] == "Maths"
    assert "created_at" in response.json()
    assert "updated_at" in response.json()

def test_subjects_returns_all_subject_data(client):
    first_response = client.post("/subjects/", json={"name": "Maths"})
    second_response = client.post("/subjects/", json={"name": "English"})
    response = client.get("/subjects/")

    assert response.status_code == 200
    assert response.json() == [first_response.json(), second_response.json()]

def test_create_duplicate_subject_returns_error409(client):
    client.post("/subjects/", json={"name": "Maths"})
    response = client.post("/subjects/", json={"name": "Maths"})

    assert response.status_code == 409
    assert response.json() == {"detail": "Subject already exists"}

def test_create_subject_strips_name_whitespace(client):
    response = client.post("/subjects/", json={"name": "  Maths  "})

    assert response.status_code == 200
    assert response.json()["name"] == "Maths"

def test_create_subject_with_empty_name_returns_error422(client):
    response = client.post("/subjects/", json={"name": "   "})

    assert response.status_code == 422
    assert response.json()["detail"][0]["loc"] == ["body", "name"]
    assert response.json()["detail"][0]["msg"] == "Value error, Name cannot be empty"

def test_create_subject_without_name_returns_error422(client):
    response = client.post("/subjects/", json={})

    assert response.status_code == 422
    assert response.json()["detail"][0]["loc"] == ["body", "name"]
    assert response.json()["detail"][0]["msg"] == "Field required"
