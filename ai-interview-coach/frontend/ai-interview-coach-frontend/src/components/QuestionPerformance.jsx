

function QuestionPerformance({ questions }) {

    return (

        <div
            style={{
                background: "#ffffff",
                border: "1px solid #ddd",
                borderRadius: "15px",
                padding: "30px",
                marginBottom: "30px",
                boxShadow: "0 3px 10px rgba(0,0,0,0.08)"
            }}
        >

            <h2
                style={{
                    marginTop: 0,
                    marginBottom: "25px",
                    color: "#1976d2"
                }}
            >
                📊 Question Performance
            </h2>

            {questions.map((question, index) => (

                <div
                    key={index}
                    style={{
                        marginBottom: "25px"
                    }}
                >

                    <div
                        style={{
                            display: "flex",
                            justifyContent: "space-between",
                            marginBottom: "8px"
                        }}
                    >

                        <div>

                            <strong>
                                Question {index + 1}
                            </strong>

                            <p
                                style={{
                                    margin: "5px 0",
                                    color: "#555"
                                }}
                            >
                                {question.question}
                            </p>

                        </div>

                        <div
                            style={{
                                fontWeight: "bold",
                                color: "#1976d2",
                                minWidth: "70px",
                                textAlign: "right"
                            }}
                        >
                            {question.score}/10
                        </div>

                    </div>

                    <div
                        style={{
                            width: "100%",
                            height: "10px",
                            background: "#eee",
                            borderRadius: "10px",
                            overflow: "hidden"
                        }}
                    >

                        <div
                            style={{
                                width: `${question.score * 10}%`,
                                height: "100%",
                                background: "#1976d2"
                            }}
                        />

                    </div>

                </div>

            ))}

        </div>

    );

}

export default QuestionPerformance;