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
    data = response.json()
    assert response.status_code == 200
    assert "access_token" in data and isinstance(data["access_token"], str)
    assert "token_type" in data and data["token_type"] == "Bearer"
    assert "account" in data
    assert "id" in data["account"] and isinstance(data["account"]["id"], int)
    assert "username" in data["account"] and isinstance(
        data["account"]["username"], str
    )
    assert "password" in data["account"] and isinstance(
        data["account"]["password"], str
    )
    assert "name" in data["account"] and isinstance(
        data["account"]["name"], str
    )
    assert "score" in data["account"] and isinstance(
        data["account"]["score"], int
    )
