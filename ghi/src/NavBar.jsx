import React, { useState } from "react";
import "./NavBar.css";
const NavBar = () => {
  const [isNavOpen, setIsNavOpen] = useState(false);
  const toggleNav = () => {
    setIsNavOpen(!isNavOpen);
  };
  return (
    <div className={`nav-container ${isNavOpen ? "open" : ""}`}>
      <button onClick={toggleNav} className="toggle-button">
        ≡
      </button>
      <div className="nav-links">
        <a href="#">Home</a>
        <a href="#">Sign In</a>
        <a href="#">Sign Up</a>
        <a href="#">Leaderboard</a>
        <a href="#">My Account</a>
        <a href="#">About Us</a>
      </div>
    </div>
  );
};
export default NavBar;
