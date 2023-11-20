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
    def get_one_user(self, user_id: int) -> Optional[UserModelOut]:
        try:
            # connect to the database
            with pool.connection() as conn:
                # get a named cursor (something to run SQL with)
                with conn.cursor(name="get_one_user") as db:
                    # Run our SELECT statement
                    db.execute(
                        """
                        SELECT id, username, password, name, score
                        FROM users
                        WHERE id = %s
                        """,
                        [user_id],
                    )
                    record = db.fetchone()
                    if record is None:
                        return None
                    print(record)
                    return self.record_to_user_out(record)
        except Exception as e:
            print(e)
            return {"message": "Could not find that user"}

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

    def record_to_user_out(self, record):
        return UserModelOut(
            id=record[0],
            username=record[1],
            password=record[2],
            name=record[3],
            score=record[4],
        )

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
