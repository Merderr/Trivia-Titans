import React, { useState } from "react";
import NavBar from "./NavBar";
import PlayButton from "./components/PlayButton";
import "./Home.css";

function Home() {
  const [count, setCount] = useState(0);

  return (
    <>
      <header className="app-header">
        <NavBar />
      </header>
      <div>
        <h1 className="title">TRIVIA TITANS</h1>
      </div>
      <div className="PlayButton">
        <PlayButton />
      </div>
    </>
  );
}

export default Home;
