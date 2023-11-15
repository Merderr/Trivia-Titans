from queries.questions import QuestionModelIn, QuestionModelOut, Error
from queries.questions import QuestionRepository
from fastapi import APIRouter, Depends, Response
from typing import Union, List, Optional

router = APIRouter()


TRIVIA_API = "https://opentdb.com/api.php?amount=1&type=multiple"


@router.get("/questions", response_model=Union[List[QuestionModelOut], Error])
def get_questions(
    repo:  QuestionRepository = Depends(),
):
    return repo.get_questions()


@router.post("/questions", response_model=Union[QuestionModelOut, Error])
def create_question(
    question: QuestionModelIn,
    response: Response,
    repo: QuestionRepository = Depends()
):
    return repo.create(question)

@router.get("/questions/{question_id}", response_model=Optional[QuestionModelOut])
def get_one_question(
    question_id: int,
    response: Response,
    repo: QuestionRepository = Depends(),
) -> Optional[QuestionModelOut]:
    question = repo.get_one(question_id)
    if question is None:
        response.status_code = 404
    return question
