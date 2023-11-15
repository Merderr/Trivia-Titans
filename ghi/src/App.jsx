import React, { useState } from "react";
import reactLogo from "./assets/react.svg";
import viteLogo from "/vite.svg";
import "./App.css";
import NavBar from "./NavBar";
import PlayButton from "./PlayButton";
import Signup from "./components/SignUp";
import Login from "./components/Login";

function App() {
  const [count, setCount] = useState(0);
  return (
    <>
      <header className="app-header">
        <NavBar />
      </header>
      <div className="content-container"></div>
      <h1>Trivia Titans</h1>
      <div className="PlayButton">
        <PlayButton />
        <p></p>
      </div>
      <Routes>
        <Route exact path="/" element={<Main />} />
        <Route exact path="/signup" element={<Signup />} />
        <Route exact path="/login" element={<Login />} />
      </Routes>
    </>
  );
}
export default App;
