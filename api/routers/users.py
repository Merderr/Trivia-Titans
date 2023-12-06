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


class AccountToken(Token):
    account: UserModelOut


class HttpError(BaseModel):
    detail: str


class UserScoreUpdate(BaseModel):
    score: int


router = APIRouter()


@router.put("/api/users/{user_id}/update-score", response_model=UserModelOut)
async def update_user_score(
    user_id: int,
    score_data: UserScoreUpdate,
    repo: UserRepository = Depends(),
):
    user = repo.get_user_by_id(user_id)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User Not Found"
        )
    user = repo.update_user_score(user_id, score_data.score)

    return user


@router.post("/api/users", response_model=UserToken | HttpError)
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


@router.get("/api/users", response_model=List[UserModelOut] | dict)
async def get_all_users(repo: UserRepository = Depends()):
    return repo.get_all_users()


@router.get("/api/users/{user_id}", response_model=UserModelOut)
async def get_user(user_id: int, repo: UserRepository = Depends()):
    user = repo.get_user_by_id(user_id)
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
    user = repo.get_user_by_id(user_id)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )

    hashed_password = authenticator.hash_password(info.password)

    info_dict = dict(info)

    updated_user = repo.update_user(user_id, info_dict, hashed_password)

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
    repo.delete_user(user_id)
    return Response(
        content=json.dumps({"message": "User deleted successfully"}),
        status_code=status.HTTP_200_OK,
        media_type="application/json",
    )


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
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found",
        )


@router.get("/leaderboard")
def get_leaderboard_route(
    queries: UserRepository = Depends(),
):
    leaderboard = queries.get_leaderboard()
    return leaderboard
