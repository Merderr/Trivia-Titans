from pydantic import BaseModel
from passlib.hash import bcrypt


class UserModel(BaseModel):
    username: str
    password: str
    name: str
    score: int

    def verify_password(self, plain_password: str):
        return bcrypt.verify(plain_password, self.password)

    @classmethod
    def create_password_hash(cls, password: str):
        return bcrypt.hash(password)
