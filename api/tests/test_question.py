from fastapi.testclient import TestClient
from fastapi import APIRouter
from main import app
from pydantic import BaseModel
from authenticator import authenticator
from queries.questions import QuestionRepository, QuestionModelOut


#Taylor's Unit Test


router = APIRouter()
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


class FakeQuestionRepo():
    def get_one_question(self, question_id):
        if question_id >= 10000:
            return None

        return QuestionModelOut(
            id=question_id,
            category="string",
            type="string",
            difficulty="string",
            question="string",
            correct_answer="string",
            incorrect_answer_1="string",
            incorrect_answer_2="string",
            incorrect_answer_3="string",
        )


def test_get_question_two():
    # Arrange
    app.dependency_overrides[QuestionRepository] = FakeQuestionRepo

    # Act
    response = client.get("/api/questions/1")
    response2 = client.get("/api/questions/10000")

    # Clean up
    app.dependency_overrides = {}

    # Assert
    assert response.status_code == 200
    assert response.json() == QuestionModelOut(
            id=1,
            category="string",
            type="string",
            difficulty="string",
            question="string",
            correct_answer="string",
            incorrect_answer_1="string",
            incorrect_answer_2="string",
            incorrect_answer_3="string",
        )
    assert response2.status_code == 404
    assert response2.json() is None
