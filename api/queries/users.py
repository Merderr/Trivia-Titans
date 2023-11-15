from pydantic import BaseModel
from passlib.hash import bcrypt
import psycopg2

DATABASE_URL = (
    "postgresql://your_username:your_password@localhost/your_database"
)
conn = psycopg2.connect(DATABASE_URL)
cursor = conn.cursor()


class UserModel(BaseModel):
    username: str
    password: str
    name: str
    score: int

    def verify_password(self, plain_password: str):
        return bcrypt.verify(plain_password, self.password)

    @classmethod
    def create_password_hash(cls, password: str):
        return bcrypt.hash(password)


def create_users_table():
    query = """
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            username TEXT UNIQUE,
            password TEXT,
            name TEXT,
            score INTEGER
        )
    """
    cursor.execute(query)
    conn.commit()


def shutdown_db():
    conn.close()


def get_user_by_username(username: str):
    query = "SELECT * FROM users WHERE username = %s"
    with conn.cursor() as cursor:
        cursor.execute(query, (username,))
        return cursor.fetchone()
