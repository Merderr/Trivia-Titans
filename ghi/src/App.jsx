import React, { useState } from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import "./App.css";
import NavBar from "./NavBar";
import PlayButton from "./PlayButton";
import Signup from "./components/SignUp";
import Login from "./components/Login";
import Main from "./components/Main";

function App() {
  const [count, setCount] = useState(0);
  return (
    <Router>
      <>
        <header className="app-header">
          <NavBar />
        </header>
        <div className="content-container">
          <Routes>
            <Route path="/" element={<Main />} />
            <Route path="/signup" element={<Signup />} />
            <Route path="/login" element={<Login />} />
          </Routes>
        </div>
        {/* <h1>Trivia Titans</h1>
        <div className="PlayButton">
          <PlayButton />
        </div> */}
      </>
    </Router>
  );
}

export default App;