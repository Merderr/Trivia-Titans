from fastapi.testclient import TestClient
from fastapi import APIRouter
from main import app


router = APIRouter()
client = TestClient(app)


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


def test_get_token():
    response = client.get("/token")

    assert response.status_code == 200
    assert "access_token" in response.json() and isinstance(
        response["access_token"], str
    )

    assert "token_type" in response.json()
    assert response.json()["token_type"] == "Bearer"
    assert "account" in response.json()
    assert "id" in response.json()["account"] and isinstance()
    assert response.json()["account"]["id"] == "string"
    assert "username" in response.json()["account"]
    assert response.json()["account"]["username"] == "string"
    assert "password" in response.json()["account"]
    assert response.json()["account"]["password"] == "string"
    assert "name" in response.json()["account"]
    assert response.json()["account"]["name"] == "string"
    assert "score" in response.json()["account"]
    assert response.json()["account"]["score"] == 0
