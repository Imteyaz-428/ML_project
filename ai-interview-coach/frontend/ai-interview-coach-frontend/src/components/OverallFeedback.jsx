

function OverallFeedback({ feedback }) {

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
                    color: "#1976d2",
                    marginBottom: "20px"
                }}
            >
                📝 Overall Feedback
            </h2>

            <p
                style={{
                    lineHeight: "1.8",
                    fontSize: "17px",
                    color: "#444"
                }}
            >
                {feedback}
            </p>

        </div>

    );

}

export default OverallFeedback;