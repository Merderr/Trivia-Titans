import React, { useState, useEffect } from "react";
import "./Game.css";

const hostURL = import.meta.env.VITE_REACT_APP_API_HOST;

const usedNumbers = [];

const Game = () => {
  const [question, setQuestion] = useState({});
  const [selectedAnswer, setSelectedAnswer] = useState(null);
  const [result, setResult] = useState(null);
  const [showModal, setShowModal] = useState(false);
  const [score, setScore] = useState(0);
  const [maxNumber, setMaxNumber] = useState(1);

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
    }
  };

  const getQuestion = async () => {
    try {
      let randomNumber;
      do {
        randomNumber = Math.floor(Math.random() * maxNumber) + 1;
      } while (usedNumbers.includes(randomNumber));

      usedNumbers.push(randomNumber);

      if (usedNumbers.length === maxNumber) {
        usedNumbers.length = 0;
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
    }
  };

  const handlePlayAgainClick = () => {
    setShowModal(false);
    setScore(0);
    getQuestion();
  };

  useEffect(() => {
    const fetchData = async () => {
      await getMaxNumber();
      getQuestion();
    };
    fetchData();
  }, [maxNumber]);

  return (
    <div className="game-container">
      <div className="content-container">
        <h1 className="title">TRIVIA TITANS</h1>
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
          <p>Correct answer was {question.correct_answer}</p>
          <p>Play again?</p>
          <button onClick={handlePlayAgainClick}>Yes</button>
        </div>
      </div>
    </div>
  );
};

export default Game;
