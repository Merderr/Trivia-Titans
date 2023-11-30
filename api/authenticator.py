# authenticator.py
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
        # Use your repo to get the account based on the
        # username (which could be an email)
        return users.get_user(username)

    def get_account_getter(
        self,
        users: UserRepository = Depends(),
    ):
        # Return the accounts. That's it.
        return users

    def get_hashed_password(self, user: UserOutWithPassword):
        # Return the encrypted password value from your
        # account object
        print(user)
        return user["password"]

    def get_account_data_for_cookie(self, user: UserModelOut):
        # Return the username and the data for the cookie.
        # You must return TWO values from this method.
        return user["username"], UserModelOut(**user)


authenticator = MyAuthenticator(os.environ["SIGNING_KEY"])
