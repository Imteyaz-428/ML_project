import { useNavigate } from "react-router-dom";

function DashboardHeader() {

    const navigate = useNavigate();

    function logout() {

        localStorage.removeItem("token");

        navigate("/login");

    }

    return (

        <div
            style={{
                display: "flex",
                justifyContent: "space-between",
                alignItems: "center",
                marginBottom: "35px"
            }}
        >

            <div>

                <h1
                    style={{
                        margin: 0,
                        color: "#1976d2",
                        fontSize: "34px"
                    }}
                >
                    AI Interview Coach
                </h1>

                <p
                    style={{
                        marginTop: "8px",
                        color: "#666"
                    }}
                >
                    Practice smarter. Get hired faster.
                </p>

            </div>

            <button
                onClick={logout}
                style={{
                    padding: "12px 24px",
                    background: "#d32f2f",
                    color: "white",
                    border: "none",
                    borderRadius: "8px",
                    cursor: "pointer",
                    fontSize: "15px",
                    fontWeight: "bold"
                }}
            >
                Logout
            </button>

        </div>

    );

}

export default DashboardHeader;