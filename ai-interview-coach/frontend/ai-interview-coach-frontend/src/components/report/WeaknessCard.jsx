

function WeaknessCard({ weaknesses }) {

    return (

        <div
            style={{
                background: "#ffffff",
                border: "1px solid #ddd",
                borderRadius: "15px",
                padding: "25px",
                boxShadow: "0 3px 10px rgba(0,0,0,0.08)",
                height: "100%"
            }}
        >

            <h2
                style={{
                    marginTop: 0,
                    marginBottom: "20px",
                    color: "#d97706"
                }}
            >
                📈 Areas to Improve
            </h2>

            <div
                style={{
                    display: "flex",
                    flexDirection: "column",
                    gap: "15px"
                }}
            >

                {weaknesses.map((item, index) => (

                    <div
                        key={index}
                        style={{
                            display: "flex",
                            alignItems: "flex-start",
                            gap: "12px",
                            background: "#fffbeb",
                            border: "1px solid #fde68a",
                            borderRadius: "10px",
                            padding: "15px"
                        }}
                    >

                        <span
                            style={{
                                fontSize: "20px"
                            }}
                        >
                            📌
                        </span>

                        <p
                            style={{
                                margin: 0,
                                color: "#92400e",
                                lineHeight: "1.6"
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

export default WeaknessCard;