import { useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";

function Login() {

    const navigate = useNavigate();

    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");

    const [loading, setLoading] = useState(false);

    async function handleLogin(e) {

        e.preventDefault();

        setLoading(true);

        const formData = new URLSearchParams();

        formData.append("username", email);
        formData.append("password", password);

        try {

            const response = await axios.post(
                "http://127.0.0.1:8000/login",
                formData,
                {
                    headers: {
                        "Content-Type":
                            "application/x-www-form-urlencoded",
                    },
                }
            );

            localStorage.setItem(
                "token",
                response.data.access_token
            );

            alert("Login Successful");

            navigate("/");

        }

        catch (err) {

            alert(
                err.response?.data?.detail ||
                "Login Failed"
            );

        }

        finally {

            setLoading(false);

        }

    }

    return (

        <div
            style={{
                minHeight: "100vh",
                display: "flex",
                justifyContent: "center",
                alignItems: "center",
                background: "#f4f7fb"
            }}
        >

            <form
                onSubmit={handleLogin}
                style={{
                    width: "420px",
                    background: "#fff",
                    padding: "40px",
                    borderRadius: "15px",
                    boxShadow: "0 8px 30px rgba(0,0,0,0.1)"
                }}
            >

                <h1
                    style={{
                        textAlign: "center",
                        marginBottom: "10px",
                        color: "#1976d2"
                    }}
                >
                    AI Interview Coach
                </h1>

                <p
                    style={{
                        textAlign: "center",
                        color: "#666",
                        marginBottom: "35px"
                    }}
                >
                    Welcome Back 👋
                </p>

                <label>Email</label>

                <input
                    type="email"
                    placeholder="Enter your email"
                    value={email}
                    onChange={(e) =>
                        setEmail(e.target.value)
                    }
                    required
                    style={{
                        width: "100%",
                        padding: "14px",
                        marginTop: "8px",
                        marginBottom: "20px",
                        borderRadius: "8px",
                        border: "1px solid #ccc",
                        fontSize: "16px",
                        boxSizing: "border-box"
                    }}
                />

                <label>Password</label>

                <input
                    type="password"
                    placeholder="Enter your password"
                    value={password}
                    onChange={(e) =>
                        setPassword(e.target.value)
                    }
                    required
                    style={{
                        width: "100%",
                        padding: "14px",
                        marginTop: "8px",
                        marginBottom: "30px",
                        borderRadius: "8px",
                        border: "1px solid #ccc",
                        fontSize: "16px",
                        boxSizing: "border-box"
                    }}
                />

                <button
                    type="submit"
                    disabled={loading}
                    style={{
                        width: "100%",
                        padding: "15px",
                        background: "#1976d2",
                        color: "#fff",
                        border: "none",
                        borderRadius: "8px",
                        fontSize: "17px",
                        cursor: "pointer"
                    }}
                >
                    {loading
                        ? "Logging In..."
                        : "Login"}
                </button>

                <p
                    style={{
                        textAlign: "center",
                        marginTop: "25px"
                    }}
                >
                    Don't have an account?{" "}
                    <span
                        onClick={() =>
                            navigate("/register")
                        }
                        style={{
                            color: "#1976d2",
                            cursor: "pointer",
                            fontWeight: "bold"
                        }}
                    >
                        Register
                    </span>
                </p>

            </form>

        </div>

    );

}

export default Login;