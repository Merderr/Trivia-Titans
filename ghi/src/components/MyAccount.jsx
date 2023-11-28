import React, { useState, useEffect } from "react";

const hostURL = import.meta.env.VITE_REACT_APP_API_HOST;

const MyAccount = () => {
  const [userData, setUserData] = useState(null);
  const [storageUser, setStorageUser] = useState();
  const fetchUserData = async () => {
    try {
      const response = await fetch(`${hostURL}/api/users/`, {
        method: "GET",
        credentials: "include",
      });

      if (response.ok) {
        const data = await response.json();
        setUserData(data);
      } else {
        console.error("Failed to fetch user data");
      }
    } catch (error) {
      console.error("Error fetching user data:", error);
    }
  };

  useEffect(() => {
    fetchUserData();
    setStorageUser(JSON.parse(localStorage.getItem("user")))
  }, []);

  return (
    <div>
      {userData && (
        <div>
          <p>Hello, {storageUser.name}</p>
          <p>Username: {storageUser.username}</p>
          <p>High Score: {storageUser.score}</p>
        </div>
      )}
    </div>
  );
};

export default MyAccount;
