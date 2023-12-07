from fastapi.testclient import TestClient
from fastapi import APIRouter
from main import app

#Taylor's Unit Test

client = TestClient(app)


def test_get_question():
    question_id = 1
    response = client.get(f"/api/questions/{question_id}")
    data = response.json()
    assert response.status_code == 200
    assert "id" in data and isinstance(data["id"], int)
    assert "category" in data and isinstance(data["category"], str)
    assert "type" in data and isinstance(data["type"], str)
    assert "difficulty" in data and isinstance(data["difficulty"], str)
    assert "question" in data and isinstance(data["question"], str)
    assert "correct_answer" in data and isinstance(data["correct_answer"], str)
    assert "incorrect_answer_1" in data and isinstance(data["incorrect_answer_1"], str)
    assert "incorrect_answer_2" in data and isinstance(data["incorrect_answer_2"], str)
    assert "incorrect_answer_3" in data and isinstance(data["incorrect_answer_3"], str)
