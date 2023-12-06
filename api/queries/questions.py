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
    incorrect_answer_1: str
    incorrect_answer_2: str
    incorrect_answer_3: str

    class Config:
        orm_mode = True


class QuestionModelOut(BaseModel):
    id: int
    category: str
    type: str
    difficulty: str
    question: str
    correct_answer: str
    incorrect_answer_1: str
    incorrect_answer_2: str
    incorrect_answer_3: str

    class Config:
        orm_mode = True


class QuestionRepository:
    def get_one_question(self, question_id: int) -> Optional[QuestionModelOut]:
        try:
            # connect to the database
            with pool.connection() as conn:
                # get a named cursor (something to run SQL with)
                with conn.cursor(name="get_one_cursor") as db:
                    # Run our SELECT statement
                    db.execute(
                        """
                        SELECT id, category, type, difficulty, question,
                        correct_answer, incorrect_answer_1, incorrect_answer_2,
                        incorrect_answer_3
                        FROM questions
                        WHERE id = %s
                        """,
                        [question_id],
                    )
                    record = db.fetchone()
                    if record is None:
                        return None
                    print(record)
                    return self.record_to_question_out(record)
        except Exception as e:
            print(e)
            return {"message": "Could not get that question"}

    def get_questions(self) -> Union[Error, List[QuestionModelOut]]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT id, category, type, difficulty, question,
                        correct_answer, incorrect_answer_1, incorrect_answer_2,
                        incorrect_answer_3
                        FROM questions
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
                            incorrect_answer_1=record[6],
                            incorrect_answer_2=record[7],
                            incorrect_answer_3=record[8],
                        )
                        result_list.append(question)
                    return result_list
        except Exception as e:
            print(e)
            return {"message": "Could not get questions"}

    def create_all(self):
        with pool.connection() as conn:
            with conn.cursor() as db:
                db.execute(
                    """
                    INSERT INTO questions (id, category, type, difficulty, question, correct_answer, incorrect_answer_1, incorrect_answer_2, incorrect_answer_3)
                    VALUES ('Geography', 'multiple', 'easy', 'Which continent is known as the "Land Down Under"?', 'Australia', 'Africa', 'Asia', 'Europe');
                    """
                )

    def create(self, question: QuestionModelIn) -> QuestionModelOut:
        with pool.connection() as conn:
            with conn.cursor() as db:
                result = db.execute(
                    """
                    INSERT INTO questions
                        (category, type, difficulty, question,
                        correct_answer, incorrect_answer_1,
                        incorrect_answer_2, incorrect_answer_3)
                    VALUES
                        (%s, %s, %s, %s, %s, %s, %s, %s)
                    RETURNING id;
                    """,
                    [
                        question.category,
                        question.type,
                        question.difficulty,
                        question.question,
                        question.correct_answer,
                        question.incorrect_answer_1,
                        question.incorrect_answer_2,
                        question.incorrect_answer_3,
                    ],
                )
                id = result.fetchone()[0]
                return self.question_in_to_out(id, question)

    def update(
        self, question_id: int, question: QuestionModelIn
    ) -> Union[QuestionModelOut, Error]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                        UPDATE questions
                        SET category = %s
                        , type = %s
                        , difficulty = %s
                        , question = %s
                        , correct_answer = %s
                        , incorrect_answer_1 = %s
                        , incorrect_answer_2 = %s
                        , incorrect_answer_3 = %s
                        WHERE id = %s
                        """,
                        [
                            question.category,
                            question.type,
                            question.difficulty,
                            question.question,
                            question.correct_answer,
                            question.incorrect_answer_1,
                            question.incorrect_answer_2,
                            question.incorrect_answer_3,
                            question_id,
                        ],
                    )
                return self.question_in_to_out(question_id, question)
        except Exception as e:
            print(e)
            return {"message": "Could not update question"}

    def delete(self, question_id: int) -> bool:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                        DELETE  FROM questions
                        WHERE id = %s
                        """,
                        [question_id],
                    )
                    return True
        except Exception as e:
            print(e)
            return False

    def question_in_to_out(self, id: int, question: QuestionModelIn):
        old_data = question.dict()
        return QuestionModelOut(id=id, **old_data)

    def record_to_question_out(self, record):
        return QuestionModelOut(
            id=record[0],
            category=record[1],
            type=record[2],
            difficulty=record[3],
            question=record[4],
            correct_answer=record[5],
            incorrect_answer_1=record[6],
            incorrect_answer_2=record[7],
            incorrect_answer_3=record[8],
        )
