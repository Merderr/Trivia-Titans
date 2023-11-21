import React, { useState } from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import "./App.css";
import NavBar from "./NavBar";
import PlayButton from "./PlayButton";
import Signup from "./components/SignUp";
import Login from "./components/Login";
import Home from "./Home";
import Leaderboard from "./Leaderboard";
import MyAccount from "./MyAccount";
import AboutUs from "./AboutUs";
import Game from "./Game";
import { AuthProvider } from "@galvanize-inc/jwtdown-for-react";

function App() {
  const [count, setCount] = useState(0);
  return (
    <AuthProvider>
      <Router>
        <>
          <header className="app-header">
            <NavBar />
          </header>
          <div className="content-container">
            <Routes>
              <Route path="/" element={<Home />} />
              <Route path="/signup" element={<Signup />} />
              <Route path="/login" element={<Login />} />
              <Route path="/leaderboard" element={<Leaderboard />} />
              <Route path="/myaccount" element={<MyAccount />} />
              <Route path="/aboutus" element={<AboutUs />} />
              <Route path="/play" element={<Game />} />
            </Routes>
          </div>
          {/* <h1>Trivia Titans</h1>
        <div className="PlayButton">
          <PlayButton />
        </div> */}
        </>
      </Router>
    </AuthProvider>
  );
}

export default App;
