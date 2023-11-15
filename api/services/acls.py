import requests

TRIVIA_API = "https://opentdb.com/api.php?amount=1&type=multiple"

def get_trivia_question():
    try:
        response = requests.get(TRIVIA_API)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        raise Exception(f"Failed to fetch question from the external API. Error: {str(e)}")
    
#Above the html in the app.jsx file 
    const fetchTriviaQuestion = async () => {
    try {
      const questionData = await get_trivia_question();
      console.log(questionData);  
    } 
  };

#in the JSX, i put it under the other button
<button onClick={fetchTriviaQuestion}>Fetch Trivia Question</button>