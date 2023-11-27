import React from "react";
import NavBar from "./NavBar";
import PlayButton from "./components/PlayButton";
import useToken from "@galvanize-inc/jwtdown-for-react";

function Home() {
  const { isAuthenticated, user } = useToken();

console.log(user)
  return (
    <>
      <header className="app-header">
        <NavBar />
      </header>
      <div className="content-container">
        <h1>Trivia Titans</h1>
        {isAuthenticated && user && (
          <p>Welcome, {user.name}!</p>
        )}
      </div>
      <div className="PlayButton">
        <PlayButton />
      </div>
    </>
  );
}

export default Home;