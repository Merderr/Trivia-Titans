import React, { useState, useEffect } from "react";
import "./NavBar.css";
import { NavLink } from "react-router-dom";
import useToken from "@galvanize-inc/jwtdown-for-react";

const NavBar = () => {
  const [isNavOpen, setIsNavOpen] = useState(false);
  const { logout, token } = useToken();
  const [storageUser, setStorageUser] = useState();

  const toggleNav = () => {
    setIsNavOpen(!isNavOpen);
  };

  const handleLogout = async () => {
    try {
      setStorageUser(localStorage.setItem("user", "null"));
      await logout();
    } catch (error) {
      alert("Please wait for logout");
    }
    location.reload();
  };

  return (
    <div className={`nav-container ${isNavOpen ? "open" : ""}`}>
      <button onClick={toggleNav} className="toggle-button">
        =
      </button>
      <div className="nav-links">
        <NavLink to="/" activeClassName="active">
          Home
        </NavLink>
        {token ? null : (
          <>
            <NavLink to="/login" activeClassName="active">
              Log In
            </NavLink>
            <NavLink to="/signup" activeClassName="active">
              Sign Up
            </NavLink>
          </>
        )}
        <NavLink to="/leaderboard" activeClassName="active">
          Leaderboard
        </NavLink>
        <NavLink to="/myaccount" activeClassName="active">
          My Account
        </NavLink>
        <NavLink to="/aboutus" activeClassName="active">
          About Us
        </NavLink>
        <NavLink to="/" activeClassName="active" onClick={handleLogout}>
          Log Out
        </NavLink>
      </div>
    </div>
  );
};

export default NavBar;
