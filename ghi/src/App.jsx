import React, { useState } from "react";
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import "./App.css";
import NavBar from "./NavBar";
import Signup from "./components/SignUp";
import Login from "./components/Login";
import Home from "./Home";

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
            <Route path="/" element={<Home />} />
            <Route path="/signup" element={<Signup />} />
            <Route path="/login" element={<Login />} />
          </Routes>
        </div>
      </>
    </Router>
  );
}

export default App;