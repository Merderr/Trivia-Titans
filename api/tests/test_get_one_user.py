from fastapi.testclient import TestClient
from main import app
from queries.users import UserRepository, UserModelOut
from typing import Optional

client = TestClient(app)


class FakeUserRepo:
    def get_user_by_id(self, user_id: int) -> Optional[UserModelOut]:
        return {
            "id": user_id,
            "username": "test_user",
            "password": "test_password",
            "name": "Test User",
            "score": 100,
        }

    def record_to_user_out(self, record):
        return {
            "id": record[0],
            "username": record[1],
            "password": record[2],
            "name": record[3],
            "score": record[4],
        }


def test_get_user_by_id():
    app.dependency_overrides[UserRepository] = FakeUserRepo

    user_id_to_test = 1

    # Act
    response = client.get(f"/api/users/{user_id_to_test}")

    # Clean up
    app.dependency_overrides = {}

    # Assert
    assert response.status_code == 200
    expected_user = {
        "id": user_id_to_test,
        "username": "test_user",
        "password": "test_password",
        "name": "Test User",
        "score": 100,
    }
    assert response.json() == expected_user
