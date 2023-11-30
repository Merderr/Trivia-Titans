import React, { useState } from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import "./App.css";
import { BrowserRouter } from "react-router-dom";
import NavBar from "./NavBar";
import PlayButton from "./components/PlayButton";
import Signup from "./components/SignUp";
import Login from "./Login";
import Home from "./Home";
import Leaderboard from "./components/Leaderboard";
import MyAccount from "./components/MyAccount";
import AboutUs from "./components/AboutUs";
import Game from "./components/Game";
import Logout from "./Logout";
import { AuthProvider } from "@galvanize-inc/jwtdown-for-react";

function App() {
  const [count, setCount] = useState(0);
  const domain = /https:\/\/[^/]+/;
  const basename = import.meta.env.VITE_PUBLIC_URL.replace(domain, "");
  return (
    <BrowserRouter basename={basename}>
      <AuthProvider baseUrl={import.meta.env.VITE_REACT_APP_API_HOST}>
        <Router>
          <>
            <header className="app-header">
              <NavBar />
            </header>
            <div className="content-container">
              <Routes>
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
        </Router>
      </AuthProvider>
    </BrowserRouter>
  );
}

export default App;
