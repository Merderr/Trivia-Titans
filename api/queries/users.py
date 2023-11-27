from fastapi import HTTPException, status
from fastapi.responses import JSONResponse
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
            with pool.connection() as conn:
                with conn.cursor(name="get_one_user") as db:
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

    def delete_user(self, user_id: int) -> Union[None, JSONResponse]:
        try:
            print(f"Deleting user with ID: {user_id}")
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                        DELETE FROM users
                        WHERE id = %s;
                        """,
                        [int(user_id)],  # Ensure user_id is cast to int
                    )
            print(f"User with ID {user_id} deleted successfully.")
            return JSONResponse(content=None, status_code=204)
        except Exception as e:
            print(f"Error deleting user with ID {user_id}: {e}")
            return JSONResponse(
                content={"message": "Could not delete user"}, status_code=500
            )

    def update_user(
        self, user_id: int, new_info: dict, hashed_password: str
    ) -> Union[None, JSONResponse]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    if not new_info:
                        return JSONResponse(
                            content={"message": "No updates provided"},
                            status_code=422,
                        )

                    set_values = tuple(new_info.values())

                    print("SET values:", set_values)

                    set_clause = (
                        ", ".join(
                            f"{key} = %s"
                            for key in new_info.keys()
                            if key != "password"
                        )
                        or "password = %s"
                    )

                    db.execute(
                        f"""
                        UPDATE users
                        SET {set_clause}, password = %s
                        WHERE id = %s;
                        """,
                        (
                            *[
                                new_info[key]
                                for key in new_info.keys()
                                if key != "password"
                            ],
                            hashed_password,
                            user_id,
                        ),
                    )

                    return JSONResponse(content=None, status_code=200)
        except Exception as e:
            print(e)
            return JSONResponse(
                content={"message": "Could not update user"}, status_code=500
            )

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
