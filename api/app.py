from flask import Flask
import requests

# Define API URL.
TRIVIA_URL = "https://api.api-ninjas.com/v1/trivia"

# Initialize Flask.
app = Flask(__name__)


# Define routing.
@app.route("/")
def index():
    # Make API Call - make sure to use a valid API key.
    resp = requests.get(
        TRIVIA_URL,
        headers={"X-Api-Key": "3vhAqCBWX1iInV8cpSrmpQ==IAljp8SZhlfeRNRh"},
    ).json()
    # Get first trivia result since the API returns a list of results.
    trivia = resp[0]
    return trivia


@app.get("/")
def root():
    return {"message": "You hit the root path!"}


# Run the Flask app (127.0.0.1:5000 by default).
app.run()
