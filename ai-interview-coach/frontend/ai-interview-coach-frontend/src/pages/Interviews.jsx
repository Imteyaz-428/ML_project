import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import api from "../services/api";

function Interviews() {

    const navigate = useNavigate();

    const [interviews, setInterviews] = useState([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        loadInterviews();
    }, []);

    async function loadInterviews() {

        try {

            const response = await api.get("/interview/my");

            setInterviews(response.data);

        }

        catch (error) {

            console.log(error);

            alert("Failed to load interviews.");

        }

        finally {

            setLoading(false);

        }

    }

    if (loading) {

        return (
            <h2 style={{ textAlign: "center", marginTop: "100px" }}>
                Loading Interviews...
            </h2>
        );

    }

    return (

        <div
            style={{
                maxWidth: "1000px",
                margin: "40px auto",
                padding: "20px"
            }}
        >

            <h1
                style={{
                    color: "#1976d2",
                    marginBottom: "30px"
                }}
            >
                My Interviews
            </h1>

            {interviews.map((item) => (

                <div
                    key={item.id}
                    style={{
                        border: "1px solid #ddd",
                        borderRadius: "12px",
                        padding: "20px",
                        marginBottom: "20px",
                        boxShadow: "0 2px 8px rgba(0,0,0,.08)"
                    }}
                >

                    <h2>{item.company}</h2>

                    <p><b>Role:</b> {item.role}</p>

                    <p><b>Difficulty:</b> {item.difficulty}</p>

                    <p><b>Date:</b> {item.created_at.slice(0,10)}</p>

                    <button
                        onClick={() => navigate(`/report/${item.id}`)}
                        style={{
                            padding: "10px 20px",
                            background: "#1976d2",
                            color: "white",
                            border: "none",
                            borderRadius: "8px",
                            cursor: "pointer"
                        }}
                    >
                        View Report
                    </button>

                </div>

            ))}

        </div>

    );

}

export default Interviews;