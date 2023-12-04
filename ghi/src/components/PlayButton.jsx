import React from "react";
import "./PlayButton.css";

const PlayButton = () => {
  return (
    <div>
      <Link href="play" className="play-button">
        <button className="game-button">Play Now</button>
      </Link>
    </div>
  );
};
export default PlayButton;
