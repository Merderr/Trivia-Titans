from fastapi.testclient import TestClient
from main import app
from queries.users import UserRepository
from psycopg_pool import ConnectionPool

client = TestClient(app)


def test_get_all_users():
    test_user = {
        "username": "testuser",
        "password": "testpassword",
        "name": "Test User",
        "score": 100,
    }

    with UserRepository() as repo:
        hashed_password = "hashed_test_password"
        repo.create_user(test_user, hashed_password)

    response = client.get("/api/users")
    assert response.status_code == 200
    assert test_user in response.json()
