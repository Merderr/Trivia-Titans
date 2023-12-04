import React from "react";
import "./PlayButton.css";

const PlayButton = () => {
  return (
    <div>
      <a href="play" className="play-button">
        <button className="game-button">Play Now</button>
      </a>
    </div>
  );
};
export default PlayButton;
