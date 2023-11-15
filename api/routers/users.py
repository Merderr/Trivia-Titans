from fastapi import APIRouter, Depends
from queries.users import get_user_by_username

router = APIRouter()


@router.get("/users/{username}")
def get_user(username: str, db=Depends(get_user_by_username)):
    return db
