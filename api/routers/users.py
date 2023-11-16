from fastapi import APIRouter, Depends, HTTPException
from queries.users import create_user

# (
#     # get_user_by_username,
#     # get_all_users,
#     create_user
#     # update_user,
#     # delete_user,
# )
from queries.users import UserModel

router = APIRouter()


# @router.get("/users/{username}", response_model=UserModel)
# def read_user(username: str = Depends(get_user_by_username)):
#     if username:
#         return username
#     raise HTTPException(status_code=404, detail="User not found")


# @router.get("/users", response_model=list[UserModel])
# def read_users():
#     return get_all_users()


@router.post("/users", response_model=UserModel)
def create_user_route(user: UserModel):
    return create_user(user.username, user.password, user.name, user.score)


# @router.put("/users/{username}", response_model=UserModel)
# def update_user_route(username: str, new_name: str, new_score: int):
#     return update_user(username, new_name, new_score)


# @router.delete("/users/{username}", response_model=UserModel)
# def delete_user_route(username: str):
#     return delete_user(username)
