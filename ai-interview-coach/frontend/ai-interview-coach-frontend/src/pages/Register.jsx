



import { useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";

function Register() {

    const navigate = useNavigate();

    const [name, setName] = useState("");
    const [email, setEmail] = useState("");
    const [age, setAge] = useState("");
    const [gender, setGender] = useState("");
    const [trade, setTrade] = useState("");
    const [password, setPassword] = useState("");

    const [loading, setLoading] = useState(false);

    async function handleRegister(e) {

        e.preventDefault();

        setLoading(true);

        const data = {
            Name: name,
            Email: email,
            Age: age,
            Gender: gender,
            Trade: trade,
            password: password
        };

        try {

            await axios.post(
                "https://ai-interview-backend-p8gl.onrender.com/Register",
                data
            );

            alert("Registration Successful 🎉");

            navigate("/Login");

        }

        catch (error) {

            alert(
                error.response?.data?.detail ||
                "Registration Failed"
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
                onSubmit={handleRegister}
                style={{
                    width: "450px",
                    background: "#fff",
                    padding: "40px",
                    borderRadius: "15px",
                    boxShadow: "0 8px 30px rgba(0,0,0,0.1)"
                }}
            >

                <h1
                    style={{
                        textAlign: "center",
                        color: "#1976d2",
                        marginBottom: "10px"
                    }}
                >
                    AI Interview Coach
                </h1>

                <p
                    style={{
                        textAlign: "center",
                        color: "#666",
                        marginBottom: "30px"
                    }}
                >
                    Create your account 🚀
                </p>

                <input
                    type="text"
                    placeholder="Full Name"
                    value={name}
                    onChange={(e) => setName(e.target.value)}
                    required
                    style={inputStyle}
                />

                <input
                    type="email"
                    placeholder="Email"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                    required
                    style={inputStyle}
                />

                <input
                    type="number"
                    placeholder="Age"
                    value={age}
                    onChange={(e) => setAge(Number(e.target.value))}
                    required
                    style={inputStyle}
                />

                <select
                    value={gender}
                    onChange={(e) => setGender(e.target.value)}
                    required
                    style={inputStyle}
                >
                    <option value="">Select Gender</option>
                    <option value="male">Male</option>
                    <option value="female">Female</option>
                    <option value="other">Other</option>
                </select>

                <input
                    type="text"
                    placeholder="Trade / Branch"
                    value={trade}
                    onChange={(e) => setTrade(e.target.value)}
                    required
                    style={inputStyle}
                />

                <input
                    type="password"
                    placeholder="Password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    required
                    style={inputStyle}
                />

                <button
                    type="submit"
                    disabled={loading}
                    style={{
                        width: "100%",
                        padding: "15px",
                        background: "#1976d2",
                        color: "white",
                        border: "none",
                        borderRadius: "8px",
                        fontSize: "17px",
                        cursor: "pointer",
                        marginTop: "10px"
                    }}
                >
                    {loading
                        ? "Creating Account..."
                        : "Create Account"}
                </button>

                <p
                    style={{
                        marginTop: "25px",
                        textAlign: "center"
                    }}
                >
                    Already have an account?{" "}
                    <span
                        onClick={() => navigate("/Login")}
                        style={{
                            color: "#1976d2",
                            fontWeight: "bold",
                            cursor: "pointer"
                        }}
                    >
                        Login
                    </span>
                </p>

            </form>

        </div>

    );

}

const inputStyle = {
    width: "100%",
    padding: "14px",
    marginBottom: "18px",
    borderRadius: "8px",
    border: "1px solid #ccc",
    fontSize: "15px",
    boxSizing: "border-box"
};

export default Register;