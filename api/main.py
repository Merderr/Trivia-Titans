from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import questions
from routers import users
import os
from authenticator import authenticator

app = FastAPI()

origins = [
    "https://module3-project-gamma-ice-climbers-c0a68aa6a822a297eec1a4775dd1.gitlab.io/",
    "http://localhost:3000",
    "http://localhost:8000",
    "https://rc678-galvanize.gitlab.io/",
    os.environ.get("CORS_HOST", None),
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(authenticator.router)
app.include_router(questions.router, prefix="/api")
app.include_router(users.router)


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
