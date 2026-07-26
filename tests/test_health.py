def test_healthcheck_returns_success(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "message": "Student records api is currently running"
    }
