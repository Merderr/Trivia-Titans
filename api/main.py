from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from routers import questions
from routers import users
from authenticator import authenticator

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        os.environ.get(
            "https://rc678-galvanize.gitlab.io", "http://localhost:3000"
        )
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(authenticator.router)
app.include_router(questions.router, prefix="/api")
app.include_router(users.router)
app.include_router(users.router, prefix="/token")


@app.get("/api/launch-details")
def launch_details():
    return {
        "launch_details": {
            "module": 3,
            "week": 17,
            "day": 5,
            "hour": 19,
            "min": "00",
        }
    }
