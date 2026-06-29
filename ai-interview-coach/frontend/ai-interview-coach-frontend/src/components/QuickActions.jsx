import { useNavigate } from "react-router-dom";
import ActionCard from "./ActionCard";

function QuickActions() {

    const navigate = useNavigate();

    return (

        <div
            style={{
                marginBottom: "35px"
            }}
        >

            <h2
                style={{
                    marginBottom: "20px",
                    color: "#1976d2"
                }}
            >
                ⚡ Quick Actions
            </h2>

            <div
                style={{
                    display: "grid",
                    gridTemplateColumns: "repeat(auto-fit, minmax(220px, 1fr))",
                    gap: "20px"
                }}
            >

                <ActionCard
                    icon="📄"
                    title="Resume"
                    description="Upload or update your resume."
                    onClick={() => navigate("/resume")}
                />

                <ActionCard
                    icon="🎤"
                    title="Start Interview"
                    description="Begin a new AI mock interview."
                    onClick={() => navigate("/interview-setup")}
                />

                <ActionCard
                    icon="📊"
                    title="My Interviews"
                    description="View all interviews and reports."
                    onClick={() => navigate("/interviews")}
                />

                <ActionCard
                    icon="👤"
                    title="Profile"
                    description="Manage your profile information."
                    onClick={() => navigate("/profile")}
                />

            </div>

        </div>

    );

}

export default QuickActions;