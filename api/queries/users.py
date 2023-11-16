from pydantic import BaseModel
from passlib.hash import bcrypt
import psycopg

DATABASE_URL = (
    "postgresql://your_username:your_password@localhost/your_database"
)
conn = psycopg.connect(DATABASE_URL)
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


def get_all_users():
    query = "SELECT * FROM users"
    with conn.cursor() as cursor:
        cursor.execute(query)
        return cursor.fetchall()


def create_user(username: str, password: str, name: str, score: int):
    query = """
        INSERT INTO users (username, password, name, score)
        VALUES (%s, %s, %s, %s)
        RETURNING *
    """
    with conn.cursor() as cursor:
        cursor.execute(query, (username, password, name, score))
        conn.commit()
        return cursor.fetchone()


def update_user(username: str, new_name: str, new_score: int):
    query = """
        UPDATE users
        SET name = %s, score = %s
        WHERE username = %s
        RETURNING *
    """
    with conn.cursor() as cursor:
        cursor.execute(query, (new_name, new_score, username))
        conn.commit()
        return cursor.fetchone()


def delete_user(username: str):
    query = "DELETE FROM users WHERE username = %s RETURNING *"
    with conn.cursor() as cursor:
        cursor.execute(query, (username,))
        conn.commit()
        return cursor.fetchone()
