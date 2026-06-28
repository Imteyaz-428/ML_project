import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import api from "../services/api";

function Profile() {

    const navigate = useNavigate();

    const [user, setUser] = useState(null);
    const [loading, setLoading] = useState(true);

    async function loadProfile() {

        try {

            const response = await api.get("/Profile");

            setUser(response.data);

        } catch (error) {

            console.log(error);
            alert(
                error.response?.data?.detail ||
                "Failed to load profile."
            );

        } finally {

            setLoading(false);

        }

    }

    useEffect(() => {

        loadProfile();

    }, []);

    if (loading) {

        return (
            <h2
                style={{
                    textAlign: "center",
                    marginTop: "100px"
                }}
            >
                Loading Profile...
            </h2>
        );

    }

    return (

        <div
            style={{
                maxWidth: "900px",
                margin: "40px auto",
                padding: "20px"
            }}
        >

            <div
                style={{
                    background: "#fff",
                    borderRadius: "18px",
                    padding: "35px",
                    boxShadow: "0 8px 25px rgba(0,0,0,0.08)"
                }}
            >

                <div
                    style={{
                        display: "flex",
                        alignItems: "center",
                        justifyContent: "space-between",
                        marginBottom: "30px"
                    }}
                >

                    <div>

                        <h1
                            style={{
                                color: "#2563eb",
                                marginBottom: "8px"
                            }}
                        >
                            👤 My Profile
                        </h1>

                        <p
                            style={{
                                color: "#666"
                            }}
                        >
                            Manage your account information.
                        </p>

                    </div>

                    <button
                        onClick={() => navigate("/")}
                        style={{
                            background: "#2563eb",
                            color: "white",
                            border: "none",
                            padding: "12px 22px",
                            borderRadius: "10px",
                            cursor: "pointer",
                            fontWeight: "600"
                        }}
                    >
                        Dashboard
                    </button>

                </div>

                <div
                    style={{
                        display: "grid",
                        gridTemplateColumns: "1fr 1fr",
                        gap: "20px"
                    }}
                >

                    <ProfileItem
                        label="Full Name"
                        value={user?.Name}
                    />

                    <ProfileItem
                        label="Email"
                        value={user?.Email}
                    />

                    <ProfileItem
                        label="Age"
                        value={user?.Age}
                    />

                    <ProfileItem
                        label="Gender"
                        value={user?.Gender}
                    />

                    <ProfileItem
                        label="Trade"
                        value={user?.Trade}
                    />

                    <ProfileItem
                        label="Account Status"
                        value="Active"
                    />

                </div>

                <div
                    style={{
                        marginTop: "40px",
                        display: "flex",
                        gap: "15px"
                    }}
                >

                    <button
                        style={{
                            background: "#2563eb",
                            color: "white",
                            border: "none",
                            padding: "12px 25px",
                            borderRadius: "10px",
                            cursor: "pointer",
                            fontWeight: "600"
                        }}
                    >
                        Edit Profile
                    </button>

                    <button
                        style={{
                            background: "#dc2626",
                            color: "white",
                            border: "none",
                            padding: "12px 25px",
                            borderRadius: "10px",
                            cursor: "pointer",
                            fontWeight: "600"
                        }}
                    >
                        Change Password
                    </button>

                </div>

            </div>

        </div>

    );

}

function ProfileItem({ label, value }) {

    return (

        <div
            style={{
                background: "#f8fafc",
                padding: "18px",
                borderRadius: "12px",
                border: "1px solid #e5e7eb"
            }}
        >

            <p
                style={{
                    color: "#6b7280",
                    marginBottom: "8px",
                    fontSize: "14px"
                }}
            >
                {label}
            </p>

            <h3
                style={{
                    margin: 0,
                    color: "#111827"
                }}
            >
                {value}
            </h3>

        </div>

    );

}

export default Profile;