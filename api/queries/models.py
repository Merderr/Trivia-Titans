from pydantic import BaseModel
from typing import List


class QuestionModel(BaseModel):
    category: str
    type: str
    difficulty: str
    question: str
    correct_answer: str
    incorrect_answers: List[str]

    class Config:
        orm_mode = True
