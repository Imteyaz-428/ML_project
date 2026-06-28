
function ScoreCards({

    technical,

    communication,

    confidence,

    problemSolving

}) {

    const scores = [

        {
            title: "Technical",
            score: technical
        },

        {
            title: "Communication",
            score: communication
        },

        {
            title: "Confidence",
            score: confidence
        },

        {
            title: "Problem Solving",
            score: problemSolving
        }

    ];

    return (

        <div
            style={{
                display: "grid",
                gridTemplateColumns: "repeat(4,1fr)",
                gap: "20px",
                marginBottom: "30px"
            }}
        >

            {scores.map((item, index) => (

                <div
                    key={index}
                    style={{
                        background: "#ffffff",
                        border: "1px solid #ddd",
                        borderRadius: "15px",
                        padding: "25px",
                        textAlign: "center",
                        boxShadow: "0 3px 10px rgba(0,0,0,0.08)"
                    }}
                >

                    <h3
                        style={{
                            marginBottom: "15px",
                            color: "#555"
                        }}
                    >
                        {item.title}
                    </h3>

                    <div
                        style={{
                            fontSize: "38px",
                            fontWeight: "bold",
                            color: "#1976d2"
                        }}
                    >
                        {item.score}
                    </div>

                    <p
                        style={{
                            marginTop: "10px",
                            color: "#888"
                        }}
                    >
                        /100
                    </p>

                </div>

            ))}

        </div>

    );

}

export default ScoreCards;