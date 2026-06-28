function WelcomeCard({ user }) {

    return (

        <div
            style={{
                background: "white",
                borderRadius: "16px",
                padding: "35px",
                marginBottom: "30px",
                boxShadow: "0 2px 10px rgba(0,0,0,0.08)"
            }}
        >

            <h2
                style={{
                    margin: 0,
                    color: "#1976d2"
                }}
            >
                👋 Welcome Back
            </h2>

            <h1
                style={{
                    marginTop: "15px",
                    marginBottom: "10px"
                }}
            >
                {user.Name}
            </h1>

            <p
                style={{
                    color: "#666",
                    fontSize: "18px",
                    marginBottom: "20px"
                }}
            >
                {user.Trade}
            </p>

            <p
                style={{
                    color: "#444",
                    fontSize: "16px"
                }}
            >
                Ready for today's AI interview practice? Let's improve your interview skills.
            </p>

        </div>

    );

}

export default WelcomeCard;