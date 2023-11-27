import React from "react";
import NavBar from "./NavBar";
import PlayButton from "./components/PlayButton";
import useToken from "@galvanize-inc/jwtdown-for-react";
import "./Home.css";

function Home() {
  const { isAuthenticated, user } = useToken();

console.log(user)
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
