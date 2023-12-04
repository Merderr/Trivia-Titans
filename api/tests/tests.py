from fastapi.testclient import TestClient
from main import app


@app.get("/api/token")
async def get_token():
    return {
        "access_token": "string",
        "token_type": "Bearer",
        "account": {
            "id": 0,
            "username": "string",
            "password": "string",
            "name": "string",
            "score": 0,
        },
    }


client = TestClient(app)


def test_get_token():
    response = client.get("/token")
    assert response.status_code == 200
    assert "access_token" in response.json()
    assert response.json()["access_token"] == "string"
    assert "token_type" in response.json()
    assert response.json()["token_type"] == "Bearer"
    assert "account" in response.json()
    assert "id" in response.json()["account"]
    assert response.json()["account"]["id"] == "string"
    assert "username" in response.json()["account"]
    assert response.json()["account"]["username"] == "string"
    assert "password" in response.json()["account"]
    assert response.json()["account"]["password"] == "string"
    assert "name" in response.json()["account"]
    assert response.json()["account"]["name"] == "string"
    assert "score" in response.json()["account"]
    assert response.json()["account"]["score"] == 0



def test_get_user():
    user_id = 1
    response = client.get(f"/api/users/{user_id}")
    data = response.json()
    assert response.status_code == 200
    assert "user_id" in data and data["user_id"] == 1
    assert "username" in data and data["username"] == "expected_username"
    assert "password" in data and data["password"] == "expected_password"
    assert "name" in data and data["name"] == "expected_name"
    assert "score" in data and data["score"] == "expected_score"