import React, { useState } from "react";
import "./NavBar.css";
import { NavLink } from "react-router-dom";
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
        <NavLink to="/" activeClassName="active">
          Home
        </NavLink>
        <NavLink to="/login" activeClassName="active">
          Log In
        </NavLink>
        <NavLink to="/signup" activeClassName="active">
          Sign Up
        </NavLink>
        <NavLink to="/leaderboard" activeClassName="active">
          Leaderboard
        </NavLink>
        <NavLink to="/myaccount" activeClassName="active">
          My Account
        </NavLink>
        <NavLink to="/aboutus" activeClassName="active">
          About Us
        </NavLink>
        <NavLink to="/logout" activeClassName="active">
          Log out
        </NavLink>
      </div>
    </div>
  );
};

export default NavBar;
