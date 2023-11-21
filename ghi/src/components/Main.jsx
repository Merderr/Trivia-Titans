import "./index.css";
import PlayButton from "./PlayButton.jsx";
import { Link } from "react-router-dom";

const Main = () => {
  return (
    <div>
      <h1>Trivia Titans</h1>
      <div className="PlayButton">
        <PlayButton />
      </div>
    </div>
  );
};

export default Main;
