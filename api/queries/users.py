from pydantic import BaseModel
import os
from psycopg_pool import ConnectionPool

pool = ConnectionPool(conninfo=os.environ["DATABASE_URL"])


class UserModel(BaseModel):
    username: str
    password: str
    name: str
    score: int


# def get_user_by_username(username: str):
#     query = "SELECT * FROM users WHERE username = %s"
#     with conn.cursor() as cursor:
#         cursor.execute(query, (username,))
#         return cursor.fetchone()


# def get_all_users():
#     query = "SELECT * FROM users"
#     with conn.cursor() as cursor:
#         cursor.execute(query)
#         return cursor.fetchall()


def create_user(username: str, password: str, name: str, score: int):
    query = """
        INSERT INTO users (username, password, name, score)
        VALUES (%s, %s, %s, %s)
        RETURNING *
    """
    with pool.connection() as conn:
        with conn.cursor() as cur:
            cur.execute(query, (username, password, name, score))
    return cur.fetchone()


# def update_user(username: str, new_name: str, new_score: int):
#     query = """
#         UPDATE users
#         SET name = %s, score = %s
#         WHERE username = %s
#         RETURNING *
#     """
#     with conn.cursor() as cursor:
#         cursor.execute(query, (new_name, new_score, username))
#         conn.commit()
#         return cursor.fetchone()


# def delete_user(username: str):
#     query = "DELETE FROM users WHERE username = %s RETURNING *"
#     with conn.cursor() as cursor:
#         cursor.execute(query, (username,))
#         conn.commit()
#         return cursor.fetchone()

#Mason Added this dont want to mess u up seth move down if needed

def get_leaderboard():
    query = """
        SELECT * FROM users
        ORDER BY score DESC
    """
    with pool.connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query)
            return cursor.fetchall()