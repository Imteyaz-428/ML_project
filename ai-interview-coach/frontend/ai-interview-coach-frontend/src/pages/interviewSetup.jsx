import { useState } from "react";
import { useNavigate } from "react-router-dom";
import api from "../services/api";

function InterviewSetup() {
    const navigate = useNavigate();

    const [loading, setLoading] = useState(false);

    const [company, setCompany] = useState("");
    const [role, setRole] = useState("");

    const [difficulty, setDifficulty] = useState("Medium");
    const [interviewType, setInterviewType] = useState("Technical");
    const [numberOfQuestions, setNumberOfQuestions] = useState(10);

    const companies = [
        "Google",
        "Microsoft",
        "Amazon",
        "Meta",
        "Apple",
        "Netflix",
        "Uber",
        "Adobe",
        "Oracle",
        "OpenAI",
    ];

    const roles = [
        "Software Engineer",
        "Backend Engineer",
        "Frontend Engineer",
        "Full Stack Engineer",
        "Machine Learning Engineer",
        "AI Engineer",
        "Data Scientist",
        "Data Engineer",
        "DevOps Engineer",
    ];

    async function handleGenerate() {

        if (!company || !role) {
            alert("Please select company and role.");
            return;
        }

        try {

            setLoading(true);

            const response = await api.post("/interview/create", {

                title: `${company} ${role} Interview`,

                company,

                role,

                difficulty,

                interview_type: interviewType,

                no_of_questions: numberOfQuestions,

            });

            navigate(`/interview/${response.data.id}`);

        }

        catch (error) {

            console.log(error);

            alert("Failed to create interview.");

        }

        finally {

            setLoading(false);

        }

    }

    return (

        <div
            style={{
                maxWidth: "1200px",
                margin: "40px auto",
                padding: "0 20px",
            }}
        >

            {/* Header */}

            <div
                style={{
                    display: "flex",
                    justifyContent: "space-between",
                    alignItems: "center",
                    marginBottom: "35px",
                }}
            >

                <div>

                    <h1
                        style={{
                            color: "#2563eb",
                            fontSize: "36px",
                            marginBottom: "8px",
                        }}
                    >
                        🎤 AI Interview Setup
                    </h1>

                    <p
                        style={{
                            color: "#666",
                            fontSize: "16px",
                        }}
                    >
                        Configure your personalized AI interview.
                    </p>

                </div>

                <div
                    style={{
                        display: "flex",
                        gap: "15px",
                    }}
                >

                    <button
                        onClick={() => navigate("/")}
                        style={{
                            background: "#2563eb",
                            color: "white",
                            border: "none",
                            padding: "12px 22px",
                            borderRadius: "10px",
                            cursor: "pointer",
                            fontWeight: "600",
                        }}
                    >
                        🏠 Dashboard
                    </button>

                    <button
                        onClick={() => navigate("/resume")}
                        style={{
                            background: "#10b981",
                            color: "white",
                            border: "none",
                            padding: "12px 22px",
                            borderRadius: "10px",
                            cursor: "pointer",
                            fontWeight: "600",
                        }}
                    >
                        📄 Resume
                    </button>

                </div>

            </div>

            {/* Main Grid */}

            <div
                style={{
                    display: "grid",
                    gridTemplateColumns: "650px 450px",
                    gap: "30px",
                    alignItems: "start",
                }}
            >

                {/* LEFT CARD */}

                <div
                    style={{
                        background: "white",
                        borderRadius: "16px",
                        padding: "30px",
                        boxShadow: "0 5px 20px rgba(0,0,0,0.08)",
                    }}
                >

                    <h2>Interview Configuration</h2>

                    <hr />

                    <h3>Company</h3>

                    <input
                        type="text"
                        list="company-list"
                        placeholder="Google"
                        value={company}
                        onChange={(e) => setCompany(e.target.value)}
                        style={{
                            width: "100%",
                            padding: "12px",
                            marginBottom: "20px",
                        }}
                    />

                    <datalist id="company-list">
                        {companies.map((c, index) => (
                            <option
                                key={index}
                                value={c}
                            />
                        ))}
                    </datalist>

                    <h3>Role</h3>

                    <input
                        type="text"
                        list="role-list"
                        placeholder="Backend Engineer"
                        value={role}
                        onChange={(e) => setRole(e.target.value)}
                        style={{
                            width: "100%",
                            padding: "12px",
                            marginBottom: "20px",
                        }}
                    />

                    <datalist id="role-list">
                        {roles.map((r, index) => (
                            <option
                                key={index}
                                value={r}
                            />
                        ))}
                    </datalist>

                    <h3>Difficulty</h3>

                    <div
                        style={{
                            display: "flex",
                            gap: "10px",
                            marginBottom: "25px",
                        }}
                    >

                        {["Easy", "Medium", "Hard"].map((item) => (

                            <button
                                key={item}
                                onClick={() => setDifficulty(item)}
                                style={{
                                    flex: 1,
                                    padding: "12px",
                                    border: "none",
                                    borderRadius: "8px",
                                    cursor: "pointer",
                                    background:
                                        difficulty === item
                                            ? "#2563eb"
                                            : "#eee",
                                    color:
                                        difficulty === item
                                            ? "white"
                                            : "black",
                                }}
                            >
                                {item}
                            </button>

                        ))}

                    </div>

                    <h3>Interview Type</h3>

                    <div
                        style={{
                            display: "flex",
                            flexWrap: "wrap",
                            gap: "10px",
                            marginBottom: "25px",
                        }}
                    >

                        {["Technical", "HR", "Behavioral", "Mixed"].map((item) => (

                            <button
                                key={item}
                                onClick={() => setInterviewType(item)}
                                style={{
                                    padding: "10px 18px",
                                    border: "none",
                                    borderRadius: "8px",
                                    cursor: "pointer",
                                    background:
                                        interviewType === item
                                            ? "#2563eb"
                                            : "#eee",
                                    color:
                                        interviewType === item
                                            ? "white"
                                            : "black",
                                }}
                            >
                                {item}
                            </button>

                        ))}

                    </div>

                    <h3>Questions</h3>

                    <div
                        style={{
                            display: "flex",
                            gap: "10px",
                            marginBottom: "30px",
                        }}
                    >

                        {[5, 10, 15].map((item) => (

                            <button
                                key={item}
                                onClick={() => setNumberOfQuestions(item)}
                                style={{
                                    flex: 1,
                                    padding: "12px",
                                    border: "none",
                                    borderRadius: "8px",
                                    cursor: "pointer",
                                    background:
                                        numberOfQuestions === item
                                            ? "#2563eb"
                                            : "#eee",
                                    color:
                                        numberOfQuestions === item
                                            ? "white"
                                            : "black",
                                }}
                            >
                                {item}
                            </button>

                        ))}

                    </div>

                    <button
                        onClick={handleGenerate}
                        disabled={loading}
                        style={{
                            width: "100%",
                            padding: "16px",
                            background: "#2563eb",
                            color: "white",
                            border: "none",
                            borderRadius: "10px",
                            fontSize: "17px",
                            fontWeight: "600",
                            cursor: "pointer",
                        }}
                    >
                        {loading
                            ? "Generating..."
                            : "✨ Generate Interview"}
                    </button>

                </div>

                {/* RIGHT CARD */}

                <div
                    style={{
                        background: "#fafafa",
                        borderRadius: "16px",
                        padding: "25px",
                        boxShadow: "0 5px 20px rgba(0,0,0,0.08)",
                        position: "sticky",
                        top: "20px",
                    }}
                >

                    <h2>📋 Interview Preview</h2>

                    <hr />

                    <p><strong>Company</strong><br />{company || "Not selected"}</p>

                    <p><strong>Role</strong><br />{role || "Not selected"}</p>

                    <p><strong>Difficulty</strong><br />{difficulty}</p>

                    <p><strong>Interview Type</strong><br />{interviewType}</p>

                    <p><strong>Questions</strong><br />{numberOfQuestions}</p>

                    <hr />

                    <h3>⏱ Estimated Time</h3>

                    <p>
                        {numberOfQuestions * 2} - {numberOfQuestions * 3} Minutes
                    </p>

                    <hr />

                    <h3>You'll Receive</h3>

                    <ul
                        style={{
                            lineHeight: "1.8",
                            paddingLeft: "20px",
                        }}
                    >
                        <li>✅ Resume-based questions</li>
                        <li>✅ Company-specific interview</li>
                        <li>✅ AI evaluation</li>
                        <li>✅ Detailed report</li>
                        <li>✅ Personalized recommendations</li>
                    </ul>

                    <hr />

                    <p
                        style={{
                            color: "#666",
                            lineHeight: "1.7",
                        }}
                    >
                        Your uploaded resume will be analyzed to generate
                        personalized interview questions tailored to the
                        selected company and role.
                    </p>

                </div>

            </div>

        </div>

    );

}

export default InterviewSetup;