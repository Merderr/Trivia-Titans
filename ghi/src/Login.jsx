import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import useToken from "@galvanize-inc/jwtdown-for-react";
import "./index.css";

const Login = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [errorMessage, setErrorMessage] = useState("");
  const [isError, setIsError] = useState(false);
  const navigate = useNavigate();
  const { login } = useToken();

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      console.log(username, password);
      login(username, password);
      // Handle successful login here
    } catch (error) {
      setIsError(true);
      setErrorMessage(
        "Please wait a few minutes or username/password was entered incorrectly"
      );
      setUsername("");
      setPassword("");
    }
  };

  let errorClass = isError ? "alert alert-danger" : "alert alert-danger d-none";

  return (
    <div style={{ minHeight: "100vh" }}>
      <div className="container">
        <div className="row justify-content-center">
          <div className="col-md-6">
            <div
              className="card-3d-wrap mx-auto"
              style={{ boxShadow: "0px 2px 6px rgba(0, 0, 0, 0.3)" }}
            >
              <div className="card-3d-wrapper">
                <div className="card-front">
                  <div className="center-wrap">
                    <div className="section text-center">
                      <h4 className="mb-4 pb-3">Log In</h4>
                      <form onSubmit={(e) => handleSubmit(e)}>
                        <div className="form-group">
                          <label className="form-label">
                            Enter your username:
                          </label>
                          <input
                            name="username"
                            type="text"
                            placeholder="username goes here..."
                            className="form-control"
                            autoComplete="username"
                            onChange={(e) => setUsername(e.target.value)}
                          />
                        </div>
                        <div className="form-group mt-2">
                          <label className="form-label">
                            Enter your Password:
                          </label>
                          <input
                            name="password"
                            type="password"
                            placeholder="password goes here..."
                            className="form-control"
                            autoComplete="current-password"
                            onChange={(e) => setPassword(e.target.value)}
                          />
                        </div>
                        <div className={errorClass}>{errorMessage}</div>
                        <div style={{ marginTop: "15px" }}>
                          <input
                            className="btn btn-primary"
                            type="submit"
                            value="Login"
                          />
                        </div>
                      </form>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Login;
