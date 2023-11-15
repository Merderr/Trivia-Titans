import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import "../index.css";

const Login = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [errorMessage, setErrorMessage] = useState("");
  const navigate = useNavigate();
  const [isError, setIsError] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    await login(email, password);
    if (ourToken === null) {
      setIsError(true);
      setErrorMessage(
        "Please wait a few minutes or username/password was entered incorrectly"
      );
      setEmail("");
      setPassword("");
    }
  };

  let errorClass = "alert alert-danger d-none";

  if (isError) {
    errorClass = "alert alert-danger";
  }

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
                      <form onSubmit={handleSubmit}>
                        <div className="form-group">
                          <label className="form-label">
                            Enter your email:
                          </label>
                          <input
                            name="email"
                            type="text"
                            placeholder="email goes here..."
                            className="form-control"
                            autoComplete="username"
                            onChange={(e) => setEmail(e.target.value)}
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
