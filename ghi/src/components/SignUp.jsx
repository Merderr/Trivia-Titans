import React, { useState } from "react";
import { useNavigate, Link } from "react-router-dom";

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
    console.log(e)
  };

  return (
    <div id="signup-background">
      <div className="container">
        <div className="row justify-content-center">
          <div className="col-md-6">
            <div
              className="card-3d-wrap mx-auto"
              style={{
                boxShadow: "0px 2px 6px rgba(0, 0, 0, 0.3)",
                height: "800px",
              }}
            >
              <div className="card-3d-wrapper">
                <div className="card-front">
                  <div className="center-wrap">
                    <div className="section text-center">
                      <h4 className="mb-4 pb-3"> Sign Up Here! </h4>
                      <form
                        onSubmit={handleSubmit}
                        style={{ maxWidth: "400px", maxHeight: "600px" }}
                      >
                        <div className="form-group">
                          <label className="form-label signup-margin">
                            Username:
                          </label>
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
                          <label className="form-label signup-margin">
                            First Name:
                          </label>
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
                          <label className="form-label signup-margin">
                            Last Name:
                          </label>
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
                          <label className="form-label signup-margin">
                            Email:
                          </label>
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
                          <label className="form-label signup-margin">
                            Password:
                          </label>
                          <input
                            name="password"
                            placeholder="Set a password..."
                            type="password"
                            className="form-control"
                            onChange={(e) => {
                              setPassword(e.target.value);
                            }}
                          />
                        </div>
                        <div className="form-group">
                          <label className="form-label signup-margin">
                            Confirm Password:
                          </label>
                          <input
                            name="confirm_password"
                            placeholder="Retype password..."
                            type="password"
                            className="form-control"
                            onChange={(e) => {
                              setConfirmPassword(e.target.value);
                            }}
                          />
                        </div>
                        <button type="submit" className="btn btn-primary">
                          Sign Up
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
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Signup;