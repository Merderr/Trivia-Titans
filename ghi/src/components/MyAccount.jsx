import React, { useState, useEffect } from 'react';
import './MyAccount.css'; 

const hostURL = import.meta.env.VITE_REACT_APP_API_HOST;

const MyAccount = () => {
  const [userData, setUserData] = useState(null);
  const [storageUser, setStorageUser] = useState();
  const [loading, setLoading] = useState(true);

  const fetchUserData = async () => {
    try {
      const response = await fetch(`${hostURL}/api/users`, {
        method: 'GET',
        credentials: 'include',
      });

      if (response.ok) {
        const data = await response.json();
        setUserData(data);
      } else {
        console.error('Failed to fetch user data');
        alert('Oops! Something went wrong. Please try again later.');
      }
    } catch (error) {
      console.error('Error fetching user data:', error);
      alert('Oops! Something went wrong. Please try again later.');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchUserData();
    setStorageUser(JSON.parse(localStorage.getItem("user")));
  }, []);

  return (
    <div className="account-container">
      {loading && <p>Loading...</p>}
      {userData && (
        <div className="account-card" >
          <p className="account-title">Hello, {storageUser.name}</p>
          <div className="account-info">
            <span className="info-label">Username:</span>
            <span className="info-value">{storageUser.username}</span>
          </div>
          <div className="account-info">
            <span className="info-label">High Score:</span>
            <span className="info-value">{storageUser.score}</span>
          </div>
        </div>
      )}
    </div>
  );
};

export default MyAccount;