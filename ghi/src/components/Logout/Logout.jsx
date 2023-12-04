import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import useToken from "@galvanize-inc/jwtdown-for-react";

const Logout = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const { logout } = useToken();
  const navigate = useNavigate();
  const { token } = useToken();
  const [storageUser, setStorageUser] = useState();

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await logout();
    } catch (error) {
      setErrorMessage("Please wait for logout");
    }
    navigate("/");
  };

  useEffect(() => {
    setStorageUser(localStorage.setItem("user", "null"));
  });

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
                      <h4 className="mb-4 pb-3">Log Out</h4>
                      <form onSubmit={(e) => handleSubmit(e)}>
                        <div style={{ marginTop: "15px" }}>
                          <input
                            className="btn btn-primary"
                            type="submit"
                            value="Logout"
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

export default Logout;
