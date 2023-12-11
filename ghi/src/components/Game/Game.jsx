import React, { useState, useEffect } from "react";
import "./Game.css";
import { useNavigate } from "react-router-dom";

const hostURL = import.meta.env.VITE_REACT_APP_API_HOST;

const Game = () => {
  const [question, setQuestion] = useState({});
  const [selectedAnswer, setSelectedAnswer] = useState(null);
  const [result, setResult] = useState(null);
  const [showModal, setShowModal] = useState(false);
  const [score, setScore] = useState(0);
  const [maxNumber, setMaxNumber] = useState(464);
  const [storageUser, setStorageUser] = useState(0);
  const [usedNumbers, setUsedNumbers] = useState([]);
  const navigate = useNavigate();

  const setStates = async () => {
    setQuestion({});
    setSelectedAnswer(null);
    setResult(null);
    setShowModal(false);
    setScore(0);
    setMaxNumber(464);
    setStorageUser(0);
  };

  const shuffleAnswers = (correctAnswer, incorrectAnswers) => {
    const allAnswers = [correctAnswer, ...incorrectAnswers];
    return allAnswers.sort(() => Math.random() - 0.5);
  };

  const getMaxNumber = async () => {
    const url = hostURL + `/api/questions`;
    const response = await fetch(url);

    if (response.ok) {
      const data = await response.json();
      setMaxNumber(data.length);
      getQuestion();
    }
  };

  const getQuestion = async () => {
    try {
      let randomNumber;
      do {
        randomNumber = Math.floor(Math.random() * maxNumber) + 1;
      } while (usedNumbers.includes(randomNumber));

      setUsedNumbers((prevUsedNumbers) => [...prevUsedNumbers, randomNumber]);

      if (usedNumbers.length === maxNumber) {
        setUsedNumbers([]);
      }

      const url = hostURL + `/api/questions/${randomNumber}`;
      const response = await fetch(url);

      if (response.ok) {
        const data = await response.json();
        const shuffledAnswers = shuffleAnswers(data.correct_answer, [
          data.incorrect_answer_1,
          data.incorrect_answer_2,
          data.incorrect_answer_3,
        ]);

        setQuestion({
          ...data,
          answers: shuffledAnswers,
        });
        setResult(null);
      } else {
        console.error("Failed to fetch question");
      }
    } catch (error) {
      console.error("Error fetching question:", error);
    }
  };

  const handleAnswerClick = (selectedOption) => {
    setSelectedAnswer(selectedOption);

    const isCorrect = selectedOption === question.correct_answer;

    setResult(isCorrect ? "correct" : "incorrect");

    if (isCorrect) {
      setScore((prevScore) => prevScore + 1);
      getQuestion();
    } else {
      setShowModal(true);
      setSelectedAnswer(null);
    }
  };

  const handlePlayAgainClick = async () => {
    if (storageUser && score > storageUser.score) {
      const updatedUser = { ...storageUser, score };
      localStorage.setItem("user", JSON.stringify(updatedUser));
      setStorageUser(updatedUser);

      try {
        const userUrl = `${hostURL}/api/users/${storageUser.id}/update-score`;
        const response = await fetch(userUrl, {
          method: "PUT",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ score }),
        });

        if (response.ok) {
          console.log("User score updated successfully");
        } else {
          console.error("Failed to update user score");
        }
      } catch (error) {
        console.error("Error updating user score:", error);
      }
    }

    setShowModal(false);
    setScore(0);
    getQuestion();
    setUsedNumbers([]);
  };

  const handleNoButtonClick = () => {
    setStates();
    navigate("/");
    setUsedNumbers([]);
  };

  useEffect(() => {
    setStorageUser(JSON.parse(localStorage.getItem("user")));
    getMaxNumber();
  }, []);

  return (
    <div className="game-container">
      <div>
        <h1 className="game-title">TRIVIA TITANS</h1>
      </div>
      <div className="question-container">
        <p className="question">{question.question}</p>
      </div>
      <ul className="answer">
        {question.answers &&
          question.answers
            .reduce((rows, answer, index) => {
              if (index % 2 === 0) {
                rows.push([]);
              }
              rows[rows.length - 1].push(answer);
              return rows;
            }, [])
            .map((row, rowIndex) => (
              <div key={rowIndex} className="answer-row">
                {row.map((answer, colIndex) => (
                  <button
                    key={colIndex}
                    onClick={() => handleAnswerClick(answer)}
                    className={
                      (result === "correct" &&
                        answer === question.correct_answer &&
                        "correct") ||
                      (selectedAnswer === answer &&
                        result === "incorrect" &&
                        "incorrect") ||
                      ""
                    }
                  >
                    {answer}
                  </button>
                ))}
              </div>
            ))}
      </ul>
      <div className="score-container">
        <p>Score: {score}</p>
      </div>
      <div className={`modal-container ${showModal ? "show" : ""}`}>
        <div className="modal">
          {score > storageUser.score && (
            <p>Congratulations! You've got a new high score: {score}</p>
          )}
          <p>Correct answer was {question.correct_answer}</p>
          <p>Play again?</p>
          <button onClick={handlePlayAgainClick}>YES</button>
          <button onClick={handleNoButtonClick}>NO</button>
        </div>
      </div>
    </div>
  );
};

export default Game;
