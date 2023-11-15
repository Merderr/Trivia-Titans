from typing import List
from pydantic import BaseModel


class User(BaseModel):
    username: str
    scores: List[int] = []

    def add_score(self, score: int):
        self.scores.append(score)

    def get_total_score(self):
        return sum(self.scores)
