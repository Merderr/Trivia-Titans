import React, { useState, useEffect } from "react";
import { getLeaderboard } from "../../api/queries/users";

const Leaderboard = () => {
  const [leaderboard, setLeaderboard] = useState([]);

  useEffect(() => {
    getLeaderboard()
      .then((data) => setLeaderboard(data))
      .catch((error) => console.error("Error fetching leaderboard:", error));
  }, []);

  return (
    <div>
      <h2>Leaderboard</h2>
      <ul>
        {leaderboard.map((user) => (
          <li key={user.username}>
            {user.username} - Score: {user.score}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Leaderboard;
