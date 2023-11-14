import requests


TRIVIA_API = "https://opentdb.com/api.php?amount=1&type=multiple"


def get_trivia_question():
    try:
        response = requests.get(TRIVIA_API)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        raise Exception(f"Failed to fetch question from the external API. Error: {str(e)}")

