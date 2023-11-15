from api.queries.questions import QuestionModel
from api.queries.questions import QuestionRepository
from fastapi import APIRouter, Depends
from typing import Union, List, Optional

router = APIRouter()


@router.get("/questions")
def read_items():
    return {"message": "read items"}
