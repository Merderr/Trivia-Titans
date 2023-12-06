import React from "react";
import "./PlayButton.css";

const PlayButton = () => {
  return (
    <div className="play-button">
      <Link href="play">
        <button className="game-button">Play Now</button>
      </Link>
    </div>
  );
};
export default PlayButton;
