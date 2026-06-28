function QuestionCard({
    company,
    role,
    currentQuestion,
    totalQuestions,
    category,
    difficulty,
    question
}) {

    return (

        <div
            style={{
                border: "1px solid #ddd",
                borderRadius: "12px",
                padding: "25px",
                background: "white",
                marginBottom: "25px"
            }}
        >

            {/* Header */}

            <div
                style={{
                    display: "flex",
                    justifyContent: "space-between",
                    alignItems: "center",
                    marginBottom: "20px"
                }}
            >

                <div>
                    <h2 style={{ margin: 0 }}>
                        {company}
                    </h2>

                    <p
                        style={{
                            color: "#666",
                            marginTop: "5px"
                        }}
                    >
                        {role}
                    </p>
                </div>

                <div
                    style={{
                        background: "#1976d2",
                        color: "white",
                        padding: "8px 14px",
                        borderRadius: "8px",
                        fontWeight: "bold"
                    }}
                >
                    Question {currentQuestion} / {totalQuestions}
                </div>

            </div>

            <hr />

            {/* Tags */}

            <div
                style={{
                    display: "flex",
                    gap: "12px",
                    margin: "20px 0"
                }}
            >

                <span
                    style={{
                        background: "#e3f2fd",
                        color: "#1976d2",
                        padding: "6px 12px",
                        borderRadius: "20px",
                        fontSize: "14px"
                    }}
                >
                    {category}
                </span>

                <span
                    style={{
                        background: "#fff3cd",
                        color: "#856404",
                        padding: "6px 12px",
                        borderRadius: "20px",
                        fontSize: "14px"
                    }}
                >
                    {difficulty}
                </span>

            </div>

            {/* Question */}

            <div
                style={{
                    marginTop: "25px"
                }}
            >

                <h3
                    style={{
                        marginBottom: "12px"
                    }}
                >
                    Interview Question
                </h3>

                <p
                    style={{
                        fontSize: "18px",
                        lineHeight: "1.8",
                        color: "#333"
                    }}
                >
                    {question}
                </p>

            </div>

        </div>

    );

}

export default QuestionCard;