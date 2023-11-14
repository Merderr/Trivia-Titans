from api.queries.questions import QuestionModel
from api.queries.questions import QuestionRepository
from fastapi import APIRouter, Depends, Response
from typing import Union, List, Optional

router = APIRouter()


TRIVIA_API = "https://opentdb.com/api.php?amount=1&type=multiple"


@router.get("/question", response_model=List[QuestionModel])
def get_question(
    repo:  QuestionRepository = Depends(TRIVIA_API),
):
    return repo.get_question()
