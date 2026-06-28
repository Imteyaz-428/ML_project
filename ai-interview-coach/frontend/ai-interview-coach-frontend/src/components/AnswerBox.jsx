import { useState } from "react";

function AnswerBox({ onSubmit, loading }) {

    const [answer, setAnswer] = useState("");

    function handleSubmit() {

        if (answer.trim() === "") {
            alert("Please write your answer.");
            return;
        }

        onSubmit(answer);

        setAnswer("");
    }

    return (

        <div
            style={{
                border: "1px solid #ddd",
                borderRadius: "12px",
                padding: "25px",
                background: "white",
                marginTop: "25px"
            }}
        >

            <h2
                style={{
                    marginTop: 0,
                    marginBottom: "20px"
                }}
            >
                ✍ Your Answer
            </h2>

            <textarea
                value={answer}
                onChange={(e) => setAnswer(e.target.value)}
                placeholder="Type your answer here..."
                rows={10}
                style={{
                    width: "100%",
                    resize: "vertical",
                    padding: "15px",
                    fontSize: "16px",
                    lineHeight: "1.7",
                    borderRadius: "10px",
                    border: "1px solid #ccc",
                    boxSizing: "border-box",
                    outline: "none"
                }}
            />

            <div
                style={{
                    display: "flex",
                    justifyContent: "space-between",
                    alignItems: "center",
                    marginTop: "15px"
                }}
            >

                <span
                    style={{
                        color: "#777",
                        fontSize: "14px"
                    }}
                >
                    {answer.length} characters
                </span>

                <button
                    onClick={handleSubmit}
                    disabled={loading}
                    style={{
                        background: "#1976d2",
                        color: "white",
                        border: "none",
                        borderRadius: "8px",
                        padding: "12px 25px",
                        cursor: "pointer",
                        fontSize: "15px",
                        fontWeight: "bold"
                    }}
                >
                    {loading ? "Evaluating..." : "Submit Answer"}
                </button>

            </div>

        </div>

    );

}

export default AnswerBox;