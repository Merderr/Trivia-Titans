import React, { useState, useEffect } from "react";
import "./Game.css";

const Game = () => {
  const [question, setQuestion] = useState({});
  const [selectedAnswer, setSelectedAnswer] = useState(null);
  const [result, setResult] = useState(null);
  const [showModal, setShowModal] = useState(false);
  const [score, setScore] = useState(0);

  const shuffleAnswers = (correctAnswer, incorrectAnswers) => {
    const allAnswers = [correctAnswer, ...incorrectAnswers];
    return allAnswers.sort(() => Math.random() - 0.5);
  };

  const getQuestion = async () => {
    try {
      const randomNumber = Math.floor(Math.random() * 50) + 1;
      const url = `http://localhost:8000/api/questions/${randomNumber}`;
      const response = await fetch(url);

      if (response.ok) {
        const data = await response.json();
        const shuffledAnswers = shuffleAnswers(
          data.correct_answer,
          [
            data.incorrect_answer_1,
            data.incorrect_answer_2,
            data.incorrect_answer_3,
          ]
        );

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
    getQuestion();
  }, []);

  return (
    <div className="game-container">
      <div className="question-container">
        <p className="question">{question.question}</p>
      </div>
      <ul>
        {question.answers &&
          question.answers.map((answer, index) => (
            <li
              key={index}
              onClick={() => handleAnswerClick(answer)}
              className={
                (result === "correct" && answer === question.correct_answer && "correct") ||
                (selectedAnswer === answer && result === "incorrect" && "incorrect") ||
                ""
              }
            >
              {answer}
            </li>
          ))}
      </ul>
      <div className="score-container">
        <p>Score: {score}</p>
      </div>
      <div className={`modal-container ${showModal ? 'show' : ''}`}>
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