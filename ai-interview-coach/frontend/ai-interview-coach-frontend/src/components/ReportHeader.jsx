
function ReportHeader({

    company,
    role,
    overallScore,
    date

}) {

    return (

        <div
            style={{
                background: "#ffffff",
                border: "1px solid #ddd",
                borderRadius: "15px",
                padding: "35px",
                marginBottom: "30px",
                boxShadow: "0 3px 10px rgba(0,0,0,0.08)"
            }}
        >

            <div
                style={{
                    display: "flex",
                    justifyContent: "space-between",
                    alignItems: "center",
                    flexWrap: "wrap"
                }}
            >

                <div>

                    <h1
                        style={{
                            margin: 0,
                            color: "#1976d2"
                        }}
                    >
                        AI Interview Report
                    </h1>

                    <p
                        style={{
                            marginTop: "12px",
                            color: "#555",
                            fontSize: "18px"
                        }}
                    >
                        {company} • {role}
                    </p>

                    <p
                        style={{
                            color: "#888",
                            marginTop: "6px"
                        }}
                    >
                        {date}
                    </p>

                </div>

                <div
                    style={{
                        width: "140px",
                        height: "140px",
                        borderRadius: "50%",
                        background: "#1976d2",
                        color: "white",
                        display: "flex",
                        justifyContent: "center",
                        alignItems: "center",
                        flexDirection: "column"
                    }}
                >

                    <span
                        style={{
                            fontSize: "42px",
                            fontWeight: "bold"
                        }}
                    >
                        {overallScore}
                    </span>

                    <span
                        style={{
                            fontSize: "15px"
                        }}
                    >
                        Overall
                    </span>

                </div>

            </div>

        </div>

    );

}

export default ReportHeader;