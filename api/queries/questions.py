from queries.pool import pool
from pydantic import BaseModel
from typing import Optional, List, Union


class Error(BaseModel):
    message: str


class QuestionModelIn(BaseModel):
    category: str
    type: str
    difficulty: str
    question: str
    correct_answer: str
    incorrect_answers: List[str]

    class Config:
        orm_mode = True


class QuestionModelOut(BaseModel):
    id: int
    category: str
    type: str
    difficulty: str
    question: str
    correct_answer: str
    incorrect_answers: List[str]

    class Config:
        orm_mode = True


class QuestionRepository:
    def get_questions(self) -> Union[Error, List[QuestionModelOut]]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT id, category, type, difficulty, question, correct_answer, incorrect_answers
                        FROM question
                        ORDER BY category;
                        """
                    )
                    result_list = []
                    for record in result:
                        question = QuestionModelOut(
                                id=record[0],
                                category=record[1],
                                type=record[2],
                                difficulty=record[3],
                                question=record[4],
                                correct_answer=record[5],
                                incorrect_answers=record[6] if isinstance(record[6], list) else [record[6]],
                        )
                        result_list.append(question)
                    return result_list
        except Exception as e:
            print(e)
            return {"message": "Could not get questions"}

    def create(self, question: QuestionModelIn) -> QuestionModelOut:
        with pool.connection() as conn:
            with conn.cursor() as db:
                result = db.execute(
                    """
                    INSERT INTO question
                        (category, type, difficulty, question, correct_answer, incorrect_answers)
                    VALUES
                        (%s, %s, %s, %s, %s, %s)
                    RETURNING id;
                    """,
                    [
                        question.category,
                        question.type,
                        question.difficulty,
                        question.question,
                        question.correct_answer,
                        question.incorrect_answers,
                    ],
                )
                id = result.fetchone()[0]
                return self.question_in_to_out(id, question)

    def question_in_to_out(self, id: int, question: QuestionModelIn):
        old_data = question.dict()
        return QuestionModelOut(id=id, **old_data)
