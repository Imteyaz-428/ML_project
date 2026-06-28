import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

import api from "../services/api";

import DashboardHeader from "../components/DashboardHeader";
import QuickActions from "../components/QuickActions";

function Dashboard() {

    const navigate = useNavigate();

    const [user, setUser] = useState(null);

    const [loading, setLoading] = useState(true);

    async function fetchProfile() {

        try {

            const response = await api.get("/Profile");

            setUser(response.data);

        }

        catch (error) {

            console.log(error);

            localStorage.removeItem("token");

            navigate("/login");

        }

        finally {

            setLoading(false);

        }

    }

    useEffect(() => {

        fetchProfile();

    }, []);

    function handleLogout() {

        localStorage.removeItem("token");

        navigate("/login");

    }

    if (loading) {

        return (

            <div
                style={{
                    textAlign: "center",
                    marginTop: "120px",
                    fontSize: "22px"
                }}
            >
                Loading Dashboard...
            </div>

        );

    }

    return (

        <div
            style={{
                maxWidth: "1300px",
                margin: "40px auto",
                padding: "20px"
            }}
        >

            <DashboardHeader
                user={user}
                onLogout={handleLogout}
            />

            <QuickActions />

        </div>

    );

}

export default Dashboard;