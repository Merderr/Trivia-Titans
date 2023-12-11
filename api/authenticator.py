import os
from fastapi import Depends
from jwtdown_fastapi.authentication import Authenticator
from queries.users import (
    UserRepository,
    UserModelOut,
    UserOutWithPassword,
)


class MyAuthenticator(Authenticator):
    async def get_account_data(
        self,
        username: str,
        users: UserRepository,
    ):
        return users.get_user(username)

    def get_account_getter(
        self,
        users: UserRepository = Depends(),
    ):
        return users

    def get_hashed_password(self, user: UserOutWithPassword):
        print(user)
        return user["password"]

    def get_account_data_for_cookie(self, user: UserModelOut):
        return user["username"], UserModelOut(**user)


authenticator = MyAuthenticator(os.environ["SIGNING_KEY"])
