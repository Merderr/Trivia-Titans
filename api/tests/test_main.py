from fastapi.testclient import TestClient
from fastapi import APIRouter
from main import app

router = APIRouter()


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


@router.get("/api/users/1")
async def get_user():
    return {
        "id": 1,
        "username": "expected_username",
        "password": "expected_password",
        "name": "expected_name",
        "score": 100,
    }


@router.get("/api/questions/1")
async def get_question():
    return {
        "id": 1,
        "category": "expected_category",
        "type": "expected_type",
        "difficulty": "expected_difficulty",
        "question": "expected_question",
        "correct_answer": "expected_answer",
        "incorrect_answer_1": "expected_incorrect_answer_1",
        "incorrect_answer_2": "expected_incorrect_answer_2",
        "incorrect_answer_3": "expected_incorrect_answer_3",
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
    assert "score" in data and data["score"] == 100


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


def test_get_question():
    question_id = 1
    response = client.get(f"/api/users/{question_id}")
    data = response.json()
    assert response.status_code == 200
    assert "id" in data and data["id"] == 1
    assert "category" in data and data["category"] == "expected_category"
    assert "type" in data and data["type"] == "expected_type"
    assert "difficulty" in data and data["difficulty"] == "expected_difficulty"
    assert "question" in data and data["question"] == "expected_question"
    assert "correct_answer" in data and data["correct_answer"] == "expected_correct_answer"
    assert "incorrect_answer_1" in data and data["incorrect_answer_1"] == "expected_incorrect_answer_1"
    assert "incorrect_answer_2" in data and data["incorrect_answer_2"] == "expected_incorrect_answer_2"
    assert "incorrect_answer_3" in data and data["incorrect_answer_3"] == "expected_incorrect_answer_3"
