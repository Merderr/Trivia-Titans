import React from "react";
import "./PlayButton.css";

const PlayButton = () => {
  return (
    <div className="play-button">
      <a href="play">
        <button className="game-button">Play Now</button>
      </a>
    </div>
  );
};
export default PlayButton;
