from authenticator import authenticator
from main import app
from queries.users import UserRepository
<<<<<<< HEAD
from fastapi.testclient import TestClient
from contextlib import contextmanager

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
=======
<<<<<<< HEAD
from psycopg_pool import ConnectionPool
=======
from test_config import TestConfig  # Import the testing configuration
>>>>>>> 2c9ae934752f395a5bb86e6441525688853497cc

client = TestClient(app)

>>>>>>> a9242a633f401a727a2a14a6edd7be0ecce126d0

def test_get_all_users():
    with override_dependencies():
        response = client.get("/api/users")

    assert response.status_code == 200
    assert response.json() == []
