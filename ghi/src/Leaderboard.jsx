import React, { useState, useEffect } from "react";
import './Leaderboard.css';

const Leaderboard = () => {
  const [leaderboard, setLeaderboard] = useState([]);

  const get_leaderboard = async () => {
    const url = 'http://localhost:8000/leaderboard/';
    const response = await fetch(url);
    if (response.ok) {
      const data = await response.json();
      const sortedData = data.sort((a, b) => b.score - a.score);
      setLeaderboard(data);
    }
  };

  useEffect(() => {
    get_leaderboard();
  }, []);

  return (
    <div className="leaderboard-container">
      <h2>Leaderboard</h2>
      <div className="list-container">
        <ol>
          {leaderboard.map((user) => (
            <li key={user.name}>
              {user.name} - Score: {user.score}
            </li>
          ))}
        </ol>
      </div>
    </div>
  );
};

export default Leaderboard;