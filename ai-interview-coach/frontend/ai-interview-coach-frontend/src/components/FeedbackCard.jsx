function FeedbackCard({ feedback }) {

    if (!feedback) return null;

    return (

        <div
            style={{
                border: "1px solid #ddd",
                borderRadius: "12px",
                padding: "30px",
                marginTop: "30px",
                background: "#fafafa"
            }}
        >

            <h2
                style={{
                    marginTop: 0
                }}
            >
                🤖 AI Feedback
            </h2>

            <hr />

            {/* Score */}

            <div
                style={{
                    display: "flex",
                    justifyContent: "space-between",
                    alignItems: "center"
                }}
            >

                <h3>Overall Score</h3>

                <div
                    style={{
                        background: "#1976d2",
                        color: "white",
                        padding: "12px 25px",
                        borderRadius: "30px",
                        fontSize: "22px",
                        fontWeight: "bold"
                    }}
                >
                    {feedback.score}/10
                </div>

            </div>

            <hr />

            {/* Feedback */}

            <h3>Overall Feedback</h3>

            <p
                style={{
                    lineHeight: "1.8"
                }}
            >
                {feedback.feedback}
            </p>

            <hr />

            {/* Strengths */}

            <h3>✅ Strengths</h3>

            <ul>

                {(feedback.strengths || []).map((item, index) => (

                    <li
                        key={index}
                        style={{
                            marginBottom: "8px"
                        }}
                    >
                        {item}
                    </li>

                ))}

            </ul>

            <hr />

            {/* Improvements */}

            <h3>📈 Areas to Improve</h3>

            <ul>

                {(feedback.improvements || []).map((item, index) => (

                    <li
                        key={index}
                        style={{
                            marginBottom: "8px"
                        }}
                    >
                        {item}
                    </li>

                ))}

            </ul>

            <hr />

            {/* Correct Answer */}

            <h3>💡 Suggested Answer</h3>

            <div
                style={{
                    background: "#eef6ff",
                    padding: "18px",
                    borderRadius: "10px",
                    border: "1px solid #1976d2",
                    lineHeight: "1.8"
                }}
            >
                {feedback.correct_answer}
            </div>

        </div>

    );

}

export default FeedbackCard;