from pstats import Stats
import statistics
from fastapi import HTTPException
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


class UserScoreOut(BaseModel):
    name: str
    score: int

    class Config:
        orm_mode = True


class UserOutWithPassword(UserModelOut):
    hashed_password: str


class DuplicateAccountError(ValueError):
    pass


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

    def get_user(self, username: str) -> UserOutWithPassword:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                        SELECT id, username, password, name, score
                        FROM users
                        WHERE username = %s;
                        """,
                        [username],
                    )
                    record = None
                    row = db.fetchone()
                    if row is not None:
                        record = {}
                        for i, column in enumerate(db.description):
                            record[column.name] = row[i]
                    return record
        except Exception as e:
            print(e)
            return {"message": "Could not get user"}

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

    def create_user(
        self, user: UserModelIn, hashed_password: str
    ) -> UserModelOut:
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
                        hashed_password,
                        user.name,
                        user.score,
                    ],
                )
                id = result.fetchone()[0]
                return self.user_in_to_out(id, user, hashed_password)

    def update_user(self, user_id: int, updated_user_data: dict):
        query = """
            UPDATE users
            SET name = %s, score = %s
            WHERE id = %s
            RETURNING *;
        """
        values = (
            updated_user_data.get("name"),
            updated_user_data.get("score"),
            user_id,
        )

        with self.pool.connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, values)
                updated_user = cursor.fetchone()

                if not updated_user:
                    raise HTTPException(
                        status_code=Stats.HTTP_404_NOT_FOUND,
                        detail=f"User with ID {user_id} not found",
                    )

                return self.user_in_to_out(updated_user)

    def delete_user(self, user_id: int):
        query = "DELETE FROM users WHERE id = %s RETURNING *;"

        with self.pool.connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, (user_id,))
                deleted_user = cursor.fetchone()

                if not deleted_user:
                    raise HTTPException(
                        status_code=statistics.HTTP_404_NOT_FOUND,
                        detail=f"User with ID {user_id} not found",
                    )

                return deleted_user

    def user_in_to_out(self, id: int, user: UserModelOut, hashed_password):
        old_data = {
            "id": id,
            "username": user.username,
            "password": hashed_password,
            "name": user.name,
            "score": user.score,
        }
        return old_data

    def record_to_user_out(self, record) -> UserModelOut:
        return UserModelOut(
            id=record[0],
            username=record[1],
            password=record[2],
            name=record[3],
            score=record[4],
        )

    # Mason Added this dont want to mess u up seth move down if needed
    def get_leaderboard(self):
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT name, score
                        FROM users
                        ORDER BY score;
                        """
                    )
                    result_list = []
                    for record in result:
                        user = UserScoreOut(
                            name=record[0],
                            score=record[1],
                        )
                        result_list.append(user)
                    return result_list
        except Exception as e:
            print(e)
            return {"message": "Could not get leaderboard"}
