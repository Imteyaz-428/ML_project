

function RecommendationCard({ recommendations }) {

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
                🎯 AI Recommendations
            </h2>

            <div
                style={{
                    display: "flex",
                    flexDirection: "column",
                    gap: "15px"
                }}
            >

                {recommendations.map((item, index) => (

                    <div
                        key={index}
                        style={{
                            display: "flex",
                            alignItems: "flex-start",
                            gap: "15px",
                            background: "#eff6ff",
                            border: "1px solid #bfdbfe",
                            borderRadius: "12px",
                            padding: "18px"
                        }}
                    >

                        <span
                            style={{
                                fontSize: "22px"
                            }}
                        >
                            💡
                        </span>

                        <p
                            style={{
                                margin: 0,
                                color: "#1e3a8a",
                                lineHeight: "1.7"
                            }}
                        >
                            {item}
                        </p>

                    </div>

                ))}

            </div>

        </div>

    );

}

export default RecommendationCard;