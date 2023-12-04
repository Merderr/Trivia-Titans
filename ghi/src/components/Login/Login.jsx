import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import useToken from "@galvanize-inc/jwtdown-for-react";
import "./Login.css";

const Login = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [errorMessage, setErrorMessage] = useState("");
  const [isError, setIsError] = useState(false);
  const navigate = useNavigate();
  const { login } = useToken();
  const { token } = useToken();
  const [newToken, setNewToken] = useState(undefined);

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await login(username, password);
    } catch (error) {
      setIsError(true);
      setErrorMessage(
        "Please wait a few minutes or username/password was entered incorrectly"
      );
      setUsername("");
      setPassword("");
    }
  };

  useEffect(() => {
    if (token) {
      navigate("/");
    }
  }, [token]);

  let errorClass = isError ? "alert alert-danger" : "alert alert-danger d-none";

  return (
    <div className="login-container">
      <div className="login-card">
        <h1 className="login-title">LOGIN</h1>
        <form onSubmit={(e) => handleSubmit(e)}>
          <div className="form-group">
            <input
              name="username"
              type="text"
              placeholder="Username"
              className="form-control"
              autoComplete="username"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
            />
          </div>
          <div className="form-group">
            <input
              name="password"
              type="password"
              placeholder="Password"
              className="form-control"
              autoComplete="current-password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
            />
          </div>
          <div className={errorClass}>{errorMessage}</div>
          <div className="form-group">
            <button className="login-btn" type="submit" value="Login">
              Login
            </button>
          </div>
        </form>
      </div>
    </div>
  );
};

export default Login;
