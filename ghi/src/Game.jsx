import React, { useState, useEffect } from "react";
import "./Game.css";

const Game = () => {
  const [question, setQuestion] = useState({});
  const [selectedAnswer, setSelectedAnswer] = useState(null);
  const [result, setResult] = useState(null);

  const getQuestion = async () => {
    try {
      const url = 'http://localhost:8000/api/questions/50'; 
      const response = await fetch(url);

      if (response.ok) {
        const data = await response.json();
        setQuestion(data);
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
        <li
          onClick={() => handleAnswerClick(question.correct_answer)}
          className={result === "correct" ? "correct" : ""}
        >
          {question.correct_answer}
        </li>
        <li
          onClick={() => handleAnswerClick(question.incorrect_answer_1)}
          className={
            selectedAnswer === question.incorrect_answer_1 && result === "incorrect"
              ? "incorrect"
              : ""
          }
        >
          {question.incorrect_answer_1}
        </li>
        <li
          onClick={() => handleAnswerClick(question.incorrect_answer_2)}
          className={
            selectedAnswer === question.incorrect_answer_2 && result === "incorrect"
              ? "incorrect"
              : ""
          }
        >
          {question.incorrect_answer_2}
        </li>
        <li
          onClick={() => handleAnswerClick(question.incorrect_answer_3)}
          className={
            selectedAnswer === question.incorrect_answer_3 && result === "incorrect"
              ? "incorrect"
              : ""
          }
        >
          {question.incorrect_answer_3}
        </li>
      </ul>
    </div>
  );
};

export default Game;