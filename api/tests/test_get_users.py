# test_get_users.py
from dotenv import load_dotenv
load_dotenv()

from fastapi.testclient import TestClient
from main import app
from queries.users import UserRepository
from test_config import TestConfig  # Import the testing configuration

client = TestClient(app)

def test_get_all_users():
    test_user = {
        "username": "testuser",
        "password": "testpassword",
        "name": "Test User",
        "score": 100,
    }

    # Use the testing configuration for the UserRepository
    with UserRepository(config=TestConfig) as repo:
        hashed_password = "hashed_test_password"
        repo.create_user(test_user, hashed_password)

    response = client.get("/api/users")
    assert response.status_code == 200
    assert test_user in response.json()
