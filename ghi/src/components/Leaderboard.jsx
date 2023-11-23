import React, { useState, useEffect } from "react";
import "./Leaderboard.css";

const hostURL = import.meta.env.VITE_REACT_APP_API_HOST;

const Leaderboard = () => {
  const [leaderboard, setLeaderboard] = useState([]);
  const get_leaderboard = async () => {
    const url = hostURL + "/leaderboard/";
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
    <div>
      <h2>Leaderboard</h2>
      <ol>
        {leaderboard.map((user) => (
          <li key={user.name}>
            {user.name} - Score: {user.score}
          </li>
        ))}
      </ol>
    </div>
  );
};

export default Leaderboard;
