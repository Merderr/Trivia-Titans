import React, { useState } from "react";
import { useNavigate, Link } from "react-router-dom";
import "./SignUp.css";

const Signup = () => {
  const [username, setUsername] = useState("");
  const [firstName, setFirstName] = useState("");
  const [lastName, setLastName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const navigate = useNavigate();

  const handleSubmit = (e) => {
    e.preventDefault();
    const accountData = {
      email: email,
      username: username,
      password: password,
      confirm_password: confirmPassword,
      first: firstName,
      last: lastName,
    };
    register(accountData, `${process.env.REACT_APP}/api/accounts`);
    login(accountData.email, accountData.password);
    e.target.reset();
    navigate("/");
  };

  return (
            <div className="signup-container">
                <div className="signup-card">
                  <div className="section text-center">
                    <h4 className="signup-title"> Sign Up Here! </h4>
                    <form
                      onSubmit={handleSubmit}
                      style={{ maxWidth: "400px", maxHeight: "600px" }}
                    >
                      <div className="form-group">

                        <input
                          name="username"
                          placeholder="Choose a username..."
                          type="text"
                          className="form-control"
                          onChange={(e) => {
                            setUsername(e.target.value);
                          }}
                        />
                      </div>
                      <div className="form-group">
                        <input
                          name="first"
                          placeholder="First name..."
                          type="text"
                          className="form-control"
                          onChange={(e) => {
                            setFirstName(e.target.value);
                          }}
                        />
                      </div>
                      <div className="form-group">
                        <input
                          name="last"
                          placeholder="Last name..."
                          type="text"
                          className="form-control"
                          onChange={(e) => {
                            setLastName(e.target.value);
                          }}
                        />
                      </div>
                      <div className="form-group">
                        <input
                          name="email"
                          placeholder="Enter an email"
                          type="email"
                          className="form-control"
                          onChange={(e) => {
                            setEmail(e.target.value);
                          }}
                        />
                      </div>
                      <div className="form-group">
                        <input
                          name="password"
                          placeholder="Set password..."
                          type="password"
                          className="form-control"
                          onChange={(e) => {
                            setPassword(e.target.value);
                          }}
                        />
                      </div>
                      <div className="form-group">
                        <input
                          name="confirm_password"
                          placeholder="Confirm password..."
                          type="password"
                          className="form-control"
                          onChange={(e) => {
                            setConfirmPassword(e.target.value);
                          }}
                        />
                      </div>
                      <button className="signup-btn" type="submit">
                        Submit
                      </button>
                    </form>
                  </div>
                  <p
                    href="#"
                    style={{
                      color: "white",
                      textAlign: "center",
                      marginTop: "20px",
                    }}
                  >
                    Already signed up?{" "}
                    <Link to="/login" href="#" className="form-label">
                      Log in Here!
                    </Link>
                  </p>
                </div>
              </div>
  );
};

export default Signup;
