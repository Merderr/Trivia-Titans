import React from "react";
import NavBar from "../Navbar/NavBar";
import PlayButton from "../PlayButton";
import useToken from "@galvanize-inc/jwtdown-for-react";
import "./Home.css";
import { useEffect, useState } from "react";

function Home() {
  const { token } = useToken();
  const [user, setUser] = useState("");
  const [storageUser, setStorageUser] = useState("");
  const [count, setCount] = useState(0);

  const getUser = async (e) => {
    if (token !== null) {
      const getToken = await fetch(
        `${import.meta.env.VITE_REACT_APP_API_HOST}/token`,
        {
          credentials: "include",
        }
      );
      if (getToken.ok) {
        const data = await getToken.json();
        if (data) {
          setUser(data.account);
          localStorage.setItem("user", JSON.stringify(data.account));
        }
      }
    }
  };

  useEffect(() => {
    getUser();
    if (storageUser !== null){
      setStorageUser(JSON.parse(localStorage.getItem("user")));
  }
  }, []);

  return (
    <>
      <header className="app-header"></header>
      <div className="home-container">
        <div>
          <div>
            <h1 className="main-title">TRIVIA TITANS</h1>
          </div>
          {token && storageUser && (
            <div>
              <h2 className="welcome-title">Welcome, {storageUser.name} </h2>
            </div>
          )}
          <PlayButton />
        </div>
      </div>
    </>
  );
}

export default Home;
