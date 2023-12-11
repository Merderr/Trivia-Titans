import React, { useEffect, useState } from "react";
import NavBar from "../Navbar/NavBar";
import PlayButton from "../PlayButton";
import useToken from "@galvanize-inc/jwtdown-for-react";
import "./Home.css";

function Home() {
  const { token } = useToken();
  const [user, setUser] = useState("");
  const [storageUser, setStorageUser] = useState(null);

  const getUser = async () => {
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
          setStorageUser(data.account); 
        }
      }
    }
  };

  useEffect(() => {
    getUser();
  }, [token]);

  useEffect(() => {

  }, [storageUser]);

  return (
    <>
      <header className="app-header"></header>
      <div className="home-container">
        <div>
          <div>
            <h1 className="main-title">TRIVIA TITANS</h1>
          </div>
          {token && storageUser !== null && (
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
