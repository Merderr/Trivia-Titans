from queries.questions import QuestionModelIn, QuestionModelOut, Error
from queries.questions import QuestionRepository
from fastapi import APIRouter, Depends, Response, HTTPException, status
from typing import Union, List, Optional

router = APIRouter()


@router.get("/questions", response_model=Union[List[QuestionModelOut], Error])
def get_questions(repo: QuestionRepository = Depends()):
    try:
        return repo.get_questions()
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
        )


@router.post("/questions", response_model=Union[QuestionModelOut, Error])
def create_question(
    question: QuestionModelIn,
    response: Response,
    repo: QuestionRepository = Depends(),
):
    try:
        return repo.create(question)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
        )


@router.get(
    "/questions/{question_id}", response_model=Optional[QuestionModelOut]
)
def get_one_question(
    question_id: int,
    response: Response,
    repo: QuestionRepository = Depends(),
) -> Optional[QuestionModelOut]:
    try:
        question = repo.get_one_question(question_id)
        if question is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Question not found",
            )
        return question
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
        )


@router.put(
    "/questions/{question_id}", response_model=Union[QuestionModelOut, Error]
)
def update_question(
    question_id: int,
    question: QuestionModelIn,
    repo: QuestionRepository = Depends(),
) -> Union[Error, QuestionModelOut]:
    try:
        return repo.update(question_id, question)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
        )


@router.delete("/questions/{question_id}", response_model=bool)
def delete_question(
    question_id: int,
    repo: QuestionRepository = Depends(),
) -> bool:
    try:
        return repo.delete(question_id)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
        )
