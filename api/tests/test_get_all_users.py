from fastapi.testclient import TestClient
from main import app
from queries.users import UserRepository


DATABASE_URL = (
    "postgresql://exampleuser:secret@"
    "aug-2023-2-pt-db-service.default.svc.cluster.local/"
    "postgrestriviadata"
)
SIGNING_KEY = "AC8C8396F9F516FCE01A6805FF8C3D8E"


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
