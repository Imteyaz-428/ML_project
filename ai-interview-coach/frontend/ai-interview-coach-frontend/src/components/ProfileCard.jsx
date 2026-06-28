function ProfileCard({ user }) {

    return (

        <div
            style={{
                background: "white",
                borderRadius: "16px",
                padding: "30px",
                boxShadow: "0 2px 10px rgba(0,0,0,0.08)"
            }}
        >

            <h2
                style={{
                    marginTop: 0,
                    color: "#1976d2"
                }}
            >
                👤 Profile
            </h2>

            <div
                style={{
                    display: "grid",
                    gridTemplateColumns: "repeat(2,1fr)",
                    gap: "20px",
                    marginTop: "25px"
                }}
            >

                <div>
                    <p
                        style={{
                            color: "#888",
                            marginBottom: "5px"
                        }}
                    >
                        Name
                    </p>

                    <h3>{user?.Name || "Loading..."}</h3>
                </div>

                <div>
                    <p
                        style={{
                            color: "#888",
                            marginBottom: "5px"
                        }}
                    >
                        Email
                    </p>

                    <h3>{user?.Email || "Loading..."}</h3>
                </div>

                <div>
                    <p
                        style={{
                            color: "#888",
                            marginBottom: "5px"
                        }}
                    >
                        Trade
                    </p>

                    <h3>{user?.Trade || "Loading..."}</h3>
                </div>

                <div>
                    <p
                        style={{
                            color: "#888",
                            marginBottom: "5px"
                        }}
                    >
                        Age
                    </p>

                    <h3>{user?.Age || "Loading..."}</h3>
                </div>

            </div>

        </div>

    );

}

export default ProfileCard;