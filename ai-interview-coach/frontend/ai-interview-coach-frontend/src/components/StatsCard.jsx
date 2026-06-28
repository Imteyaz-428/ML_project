function StatsCard({

    title,
    value,
    subtitle,
    color = "#1976d2"

}) {

    return (

        <div
            style={{
                background: "white",
                borderRadius: "16px",
                padding: "30px",
                textAlign: "center",
                boxShadow: "0 2px 10px rgba(0,0,0,0.08)"
            }}
        >

            <p
                style={{
                    color: "#666",
                    marginBottom: "15px",
                    fontSize: "16px"
                }}
            >
                {title}
            </p>

            <h1
                style={{
                    margin: 0,
                    color: color,
                    fontSize: "42px"
                }}
            >
                {value}
            </h1>

            <p
                style={{
                    color: "#888",
                    marginTop: "12px"
                }}
            >
                {subtitle}
            </p>

        </div>

    );

}

export default StatsCard;