from fastapi.testclient import TestClient
from main import app
from queries.users import UserRepository

# Seth's Unit Test

client = TestClient(app)


class FakeUserRepo:
    def get_all_users(self):
        return []


def test_get_users():
    # Arrange
    app.dependency_overrides[UserRepository] = FakeUserRepo

    # Act
    response = client.get("/api/users/")

    # Clean up
    app.dependency_overrides = {}

    # Assert
    assert response.status_code == 200
    assert response.json() == []
