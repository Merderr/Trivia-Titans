from pydantic import BaseModel
import os
from psycopg_pool import ConnectionPool
from typing import Optional, List, Union

pool = ConnectionPool(conninfo=os.environ["DATABASE_URL"])


class Error(BaseModel):
    message: str


class UserModelIn(BaseModel):
    username: str
    password: str
    name: str
    score: int

    class Config:
        orm_mode = True


class UserModelOut(BaseModel):
    id: int
    username: str
    password: str
    name: str
    score: int

    class Config:
        orm_mode = True


class UserRepository:
    # def get_user_by_username(username: str):
    #     query = "SELECT * FROM users WHERE username = %s"
    #     with conn.cursor() as cursor:
    #         cursor.execute(query, (username,))
    #         return cursor.fetchone()

    # def get_all_users(self):
    #     query = "SELECT * FROM users"
    #     with pool.connection as conn:
    #         with conn.cursor() as cur:
    #             cur.execute(query)
    #             return cur.fetchall()

    def get_all_users(self) -> Union[Error, List[UserModelOut]]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT id, username, password, name, score
                        FROM users
                        ORDER BY id;
                        """
                    )
                    result_list = []
                    for record in result:
                        user = UserModelOut(
                            id=record[0],
                            username=record[1],
                            password=record[2],
                            name=record[3],
                            score=record[4],
                        )
                        result_list.append(user)
                    return result_list
        except Exception as e:
            print(e)
            return {"message": "Could not get users"}

    def create_user(self, user: UserModelIn) -> UserModelOut:
        with pool.connection() as conn:
            with conn.cursor() as db:
                result = db.execute(
                    """
                    INSERT INTO users
                        (username, password, name, score)
                    VALUES
                        (%s, %s, %s, %s)
                    RETURNING id;
                    """,
                    [
                        user.username,
                        user.password,
                        user.name,
                        user.score,
                    ],
                )
                id = result.fetchone()[0]
                return self.user_in_to_out(id, user)

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

    def user_in_to_out(self, id: int, user: UserModelIn):
        old_data = user.dict()
        return UserModelOut(id=id, **old_data)

    # Mason Added this dont want to mess u up seth move down if needed
    # def get_leaderboard():
    #     query = """
    #         SELECT * FROM users
    #         ORDER BY score DESC
    #     """
    #     with pool.connection() as conn:
    #         with conn.cursor() as cursor:
    #             cursor.execute(query)
    #             return cursor.fetchall()
