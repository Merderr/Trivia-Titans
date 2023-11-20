import React, { useState, useEffect } from "react";

const Leaderboard = () => {
  const [leaderboard, setLeaderboard] = useState([]);
  const get_leaderboard = async () => {
    const url = 'http://localhost:8000/leaderboard/';
    const response = await fetch(url);
    if (response.ok) {
      const data = await response.json();
      setLeaderboard(data);
    }
    }

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