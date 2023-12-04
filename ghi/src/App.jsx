import React, { useState } from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import "./App.css";
import NavBar from "./components/Navbar/NavBar";
import PlayButton from "./components/PlayButton";
import Signup from "./components/SignUp/SignUp";
import Login from "./components/Login/Login";
import Home from "./components/Home/Home";
import Leaderboard from "./components/Leaderboard/Leaderboard";
import MyAccount from "./components/MyAccount/MyAccount";
import AboutUs from "./components/AboutUs/AboutUs";
import Game from "./components/Game/Game";
import Logout from "./components/Logout/Logout";
import { AuthProvider } from "@galvanize-inc/jwtdown-for-react";

function App() {
  const [count, setCount] = useState(0);
  const domain = /https?:\/\/[^/]+/;
  const basename = import.meta.env.VITE_PUBLIC_URL.replace(domain, "");
  console.log(basename);
  return (
    <Router basename={basename}>
      <AuthProvider baseUrl={import.meta.env.VITE_REACT_APP_API_HOST}>
        <>
          <header className="app-header"></header>
          <NavBar />
          <div className="content-container">
            <Routes>
              <Route path="/" element={<Home />} />
              <Route path="/signup" element={<Signup />} />
              <Route path="/login" element={<Login />} />
              <Route path="/leaderboard" element={<Leaderboard />} />
              <Route path="/myaccount" element={<MyAccount />} />
              <Route path="/aboutus" element={<AboutUs />} />
              <Route path="/play" element={<Game />} />
              <Route path="/logout" element={<Logout />} />
            </Routes>
          </div>
        </>
      </AuthProvider>
    </Router>
  );
}

export default App;
