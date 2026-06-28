import { useNavigate } from "react-router-dom";

function RecentInterviewCard({

    company,
    role,
    score,
    date,
    interviewId

}) {

    const navigate = useNavigate();

    return (

        <div
            style={{
                background: "white",
                borderRadius: "16px",
                padding: "30px",
                boxShadow: "0 2px 10px rgba(0,0,0,0.08)"
            }}
        >

            <h2
                style={{
                    marginTop: 0,
                    color: "#1976d2"
                }}
            >
                📋 Recent Interview
            </h2>

            <hr
                style={{
                    margin: "20px 0"
                }}
            />

            <p>
                <strong>🏢 Company</strong><br />
                {company}
            </p>

            <p>
                <strong>💼 Role</strong><br />
                {role}
            </p>

            <p>
                <strong>⭐ Score</strong><br />
                {score}/100
            </p>

            <p>
                <strong>📅 Date</strong><br />
                {date}
            </p>

            <button
                onClick={() => navigate(`/report/${interviewId}`)}
                style={{
                    width: "100%",
                    marginTop: "15px",
                    padding: "12px",
                    background: "#1976d2",
                    color: "white",
                    border: "none",
                    borderRadius: "8px",
                    cursor: "pointer",
                    fontSize: "15px"
                }}
            >
                View Report
            </button>

        </div>

    );

}

export default RecentInterviewCard;