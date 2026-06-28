function ProgressCard({

    resumeUploaded,
    interviewsCompleted,
    averageScore

}) {

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
                📈 Your Progress
            </h2>

            <div
                style={{
                    display: "flex",
                    flexDirection: "column",
                    gap: "18px",
                    marginTop: "25px"
                }}
            >

                <div
                    style={{
                        display: "flex",
                        justifyContent: "space-between"
                    }}
                >
                    <span>📄 Resume Uploaded</span>

                    <strong>
                        {resumeUploaded ? "✅ Yes" : "❌ No"}
                    </strong>
                </div>

                <div
                    style={{
                        display: "flex",
                        justifyContent: "space-between"
                    }}
                >
                    <span>🎤 Interviews Completed</span>

                    <strong>{interviewsCompleted}</strong>
                </div>

                <div
                    style={{
                        display: "flex",
                        justifyContent: "space-between"
                    }}
                >
                    <span>⭐ Average Score</span>

                    <strong>{averageScore}/100</strong>
                </div>

            </div>

        </div>

    );

}

export default ProgressCard;