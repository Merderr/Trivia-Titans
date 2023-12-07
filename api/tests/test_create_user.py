from fastapi.testclient import TestClient
from fastapi import APIRouter
from main import app


client = TestClient(app)


def test_create_user():
    user_data = {
        "username": "new_user",
        "password": "new_password",
        "name": "New User",
        "score": 50,
    }

    response = client.post("/api/users", json=user_data)

    assert response.status_code == 200
    assert "user" in response.json()
    assert "token_type" in response.json()
    assert "access_token" in response.json()["token_type"]

    # Add more assertions based on your test requirements
    assert response.json()["user"]["username"] == user_data["username"]
    assert response.json()["user"]["name"] == user_data["name"]
    assert response.json()["user"]["score"] == user_data["score"]
