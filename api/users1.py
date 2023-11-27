# router.py
from fastapi import (
    Depends,
    HTTPException,
    status,
    Response,
    APIRouter,
    Request,
)

import json
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from jwtdown_fastapi.authentication import Token
from authenticator import authenticator

from pydantic import BaseModel

from typing import List

from queries.users import (
    UserModelIn,
    UserModelOut,
    UserRepository,
    DuplicateAccountError,
)


class UserForm(BaseModel):
    username: str
    password: str


class UserToken(Token):
    user: UserModelOut


class HttpError(BaseModel):
    detail: str


router = APIRouter()


@router.post("/api/users1", response_model=UserToken | HttpError)
async def create_user(
    info: UserModelIn,
    request: Request,
    response: Response,
    repo: UserRepository = Depends(),
):
    hashed_password = authenticator.hash_password(info.password)
    try:
        user = repo.create_user(info, hashed_password)
        print(user)
    except DuplicateAccountError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Cannot create an account with those credentials",
        )
    form = UserForm(username=info.username, password=info.password)
    token = await authenticator.login(response, request, form, repo)
    return UserToken(user=user, **token.dict())


@router.get("/api/users", response_model=List[UserModelOut])
async def get_all_users(repo: UserRepository = Depends()):
    return repo.get_all_users()


@router.get("/api/users/{user_id}", response_model=UserModelOut)
async def get_user(user_id: int, repo: UserRepository = Depends()):
    user = repo.get_one_user(user_id)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )
    return user


@router.put("/api/users/{user_id}", response_model=UserModelOut)
async def update_user(
    user_id: int, info: UserModelIn, repo: UserRepository = Depends()
):
    user = repo.get_one_user(user_id)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )

    hashed_password = authenticator.hash_password(info.password)

    info_dict = dict(info)

    # Update the user's information
    updated_user = repo.update_user(user_id, info_dict, hashed_password)

    # Convert the updated user to JSON
    updated_user_json = jsonable_encoder(updated_user)

    return JSONResponse(
        content=updated_user_json,
        status_code=status.HTTP_200_OK,
    )


@router.delete("/api/users/{user_id}", response_class=Response)
async def delete_user(user_id: int, repo: UserRepository = Depends()):
    user = repo.get_one_user(user_id)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )
    repo.delete_user(user_id)  # Pass user_id instead of user object
    return Response(
        content=json.dumps({"message": "User deleted successfully"}),
        status_code=status.HTTP_200_OK,
        media_type="application/json",
    )


class AccountToken(Token):
    account: UserModelOut


@router.get("/token", response_model=AccountToken | None)
async def get_token(
    request: Request,
    account: UserModelIn = Depends(authenticator.try_get_current_account_data),
) -> AccountToken | None:
    if account and authenticator.cookie_name in request.cookies:
        return {
            "access_token": request.cookies[authenticator.cookie_name],
            "type": "Bearer",
            "account": account,
        }
