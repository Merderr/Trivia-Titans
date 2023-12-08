import React, { useState, useEffect } from "react";
import "./Leaderboard.css";

const hostURL = import.meta.env.VITE_REACT_APP_API_HOST;

const Leaderboard = () => {
  const [leaderboard, setLeaderboard] = useState([]);
  const [currentUser, setCurrentUser] = useState(null);
  const [searchTerm, setSearchTerm] = useState("");

  const getLeaderboard = async () => {
    const url = hostURL + "/leaderboard/";
    const response = await fetch(url);
    if (response.ok) {
      const data = await response.json();
      const filteredData = data.filter((user) => user.score !== 0);
      const sortedData = filteredData.sort((a, b) => b.score - a.score);
      setLeaderboard(sortedData);
    }
  };

  const fetchCurrentUser = () => {
    const storedUser = JSON.parse(localStorage.getItem("user"));

    if (storedUser) {
      setCurrentUser(storedUser.name);
    }
  };

  useEffect(() => {
    getLeaderboard();
    fetchCurrentUser();
  }, []);

  const handleSearch = (e) => {
    setSearchTerm(e.target.value);
  };

  const filteredLeaderboard = leaderboard.filter((user) =>
    user.name.toLowerCase().includes(searchTerm.toLowerCase())
  );

  return (
    <>
      <h2 className="leaderboard-title">LEADERBOARD</h2>
      <div className="leaderboard-container">
        <div className="search-container">
          <div className="search-input-container">
            <span className="search-text">Search</span>
            <input
              className="leaderboard-input"
              type="text"
              id="search"
              value={searchTerm}
              onChange={handleSearch}
              placeholder="Enter user's name"
            />
          </div>
        </div>
        <ol className="leaderboard-list">
          {filteredLeaderboard.map((user) => (
            <li
              key={user.name}
              className={`leaderboard-item ${
                user.name === currentUser ? "highlighted" : ""
              }`}
            >
              <span>{user.name}</span> - Score: {user.score}
            </li>
          ))}
        </ol>
      </div>
    </>
  );
};

export default Leaderboard;
