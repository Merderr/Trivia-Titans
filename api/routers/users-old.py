from fastapi import APIRouter, Depends, Response, HTTPException
from queries.users import UserRepository, UserModelIn, UserModelOut, Error
from typing import Union, List, Optional

router = APIRouter()


# @router.get("/users/{username}", response_model=UserModel)
# def read_user(username: str = Depends(get_user_by_username)):
#     if username:
#         return username
#     raise HTTPException(status_code=404, detail="User not found")


# @router.get("/users/{user_id}", response_model=Optional[UserModelOut])
# def get_one_user(
#     user_id: int,
#     response: Response,
#     repo: UserRepository = Depends(),
# ) -> Optional[UserModelOut]:
#     user = repo.get_one_user(user_id)
#     if user is None:
#         response.status_code = 404
#     return user


# @router.get("/users", response_model=Union[List[UserModelOut], Error])
# def get_all_users(
#     repo: UserRepository = Depends(),
# ):
#     return repo.get_all_users()


# @router.post("/users", response_model=Union[UserModelOut, Error])
# def create_user(
#     user: UserModelIn,
#     response: Response,
#     repo: UserRepository = Depends(),
# ):
#     print(user)
#     return repo.create_user(user)


# @router.put("/users/{username}", response_model=UserModel)
# def update_user_route(username: str, new_name: str, new_score: int):
#     return update_user(username, new_name, new_score)


# @router.delete("/users/{username}", response_model=UserModel)
# def delete_user_route(username: str):
#     return delete_user(username)

# @router.get("/leaderboard")
# def get_leaderboard_route(queries: UserRepository = Depends()):
#     leaderboard = queries.get_leaderboard()
#     return leaderboard
