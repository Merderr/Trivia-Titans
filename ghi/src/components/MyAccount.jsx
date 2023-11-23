import React, { useState, useEffect } from 'react';

const hostURL = import.meta.env.VITE_REACT_APP_API_HOST;

const MyAccount = () => {
  const [userData, setUserData] = useState(null);

  const fetchUserData = async () => {
    try {
      const response = await fetch(hostURL + '/api/users');//THIS NEEDS TO BE CHANGED WHEN SETH MAKES A GET ONE USER ENDPOINT
      if (response.ok) {
        const data = await response.json();
        setUserData(data);
      } else {
        console.error('Failed to fetch user data');
      }
    } catch (error) {
      console.error('Error fetching user data:', error);
    }
  };

  useEffect(() => {
    fetchUserData();
  }, []);

  return (
    <div>
      <header>My Account</header>
      {userData && (
        <div>
          <p>Hello, {userData.name}</p>
          <p>Username: {userData.username}</p>
          <p>High Score: {userData.score}</p>
        </div>
      )}
    </div>
  );
};

export default MyAccount;
