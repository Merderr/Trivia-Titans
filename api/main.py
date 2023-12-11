from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import questions
from routers import users
import os
from authenticator import authenticator

app = FastAPI()

url = (
    "https://module3-project-gamma-ice-"
    "climbers-c0a68aa6a822a297eec1a4775dd1.gitlab.io"
)

origins = [
    "http://localhost:3000",
    "http://localhost:8000",
    "https://ice-climbers.gitlab.io",
    "https://aug-2023-2-pt-api.mod3projects.com",
    url,
    os.environ.get("CORS_HOST", None),
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(authenticator.router)
app.include_router(questions.router, prefix="/api")
app.include_router(users.router)


@app.get("/")
def root():
    return {"message": "You hit the root path! Trivia Titans"}


@app.get("/api/launch-details")
def launch_details():
    return {
        "launch_details": {
            "module": 3,
            "week": 17,
            "day": 5,
            "hour": 50,
            "min": "11",
        }
    }
