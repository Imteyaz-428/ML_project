function ActionCard({

    icon,
    title,
    description,
    onClick

}) {

    return (

        <div
            onClick={onClick}
            style={{
                background: "white",
                borderRadius: "16px",
                padding: "30px",
                textAlign: "center",
                cursor: "pointer",
                boxShadow: "0 2px 10px rgba(0,0,0,0.08)",
                transition: "0.3s"
            }}
        >

            <div
                style={{
                    fontSize: "45px",
                    marginBottom: "15px"
                }}
            >
                {icon}
            </div>

            <h3
                style={{
                    marginBottom: "10px"
                }}
            >
                {title}
            </h3>

            <p
                style={{
                    color: "#666",
                    fontSize: "15px"
                }}
            >
                {description}
            </p>

        </div>

    );

}

export default ActionCard;