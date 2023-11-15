from queries.pool import pool
from pydantic import BaseModel
from typing import Optional, List, Union


class QuestionModel(BaseModel):
    category: str
    type: str
    difficulty: str
    question: str
    correct_answer: str
    incorrect_answers: List[str]

    class Config:
        orm_mode = True


class QuestionRepository:
    def get_question(self) -> List[QuestionModel]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT category, type, difficulty, question, correct_answer, incorrect_answers
                        FROM question
                        ORDER BY category;
                        """
                    )
                    result = []
                    for record in db:
                        question = QuestionModel(
                            category=record[0],
                            type=record[1],
                            difficulty=record[2],
                            question=record[3],
                            correct_answer=record[4],
                            incorrect_answers=record[5],
                        )
                        result.append(question)
                    return result
        except Exception as e:
            print(e)
            return {"message": "Could not get question"}
