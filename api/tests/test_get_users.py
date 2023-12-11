# Mason's Unit Test
from authenticator import authenticator
from main import app
from queries.users import UserRepository
from fastapi.testclient import TestClient
from contextlib import contextmanager


DATABASE_URL = (
    "postgresql://exampleuser:secret@"
    "aug-2023-2-pt-db-service.default.svc.cluster.local/"
    "postgrestriviadata"
)
SIGNING_KEY = "AC8C8396F9F516FCE01A6805FF8C3D8E"

client = TestClient(app)


@contextmanager
def override_dependencies():
    app.dependency_overrides[authenticator.get_account_data] = fake_account
    app.dependency_overrides[UserRepository] = TestUserRepository
    yield
    app.dependency_overrides.clear()


class TestUserRepository:
    def get_all_users(self, id: int = None):
        return []


def fake_account():
    return {"id": "1", "username": "user"}


def test_get_all_users():
    with override_dependencies():
        response = client.get("/api/users")

    assert response.status_code == 200
    assert response.json() == []
