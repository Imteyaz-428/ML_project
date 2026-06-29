import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";

import api from "../services/api";

import ReportHeader from "../components/report/ReportHeader";
import OverallFeedback from "../components/report/OverallFeedback";
import StrengthCard from "../components/report/StrengthCard";
import WeaknessCard from "../components/report/WeaknessCard";
import RecommendationCard from "../components/report/RecommendationCard";
import StrongDomainsSection from "../components/report/StrongDomainsSection";
import WeakDomainsSection from "../components/report/WeakDomainsSection";
import WeakSkillsSection from "../components/report/WeakSkillsSection";
import HiringDecisionSection from "../components/report/HiringDecisionSection";


function Report() {

    const { id } = useParams();

    const [report, setReport] = useState(null);

    const [loading, setLoading] = useState(true);

    async function loadReport() {

        try {

            const response = await api.get(`/report/${id}`);

            setReport(response.data);

        }

        catch (error) {

            console.log(error);

            alert(
                error.response?.data?.detail ||
                "Unable to load report."
            );

        }

        finally {

            setLoading(false);

        }

    }

    useEffect(() => {

        loadReport();

    }, [id]);

    if (loading) {

        return (
            <h2
                style={{
                    textAlign: "center",
                    marginTop: "100px"
                }}
            >
                Loading Report...
            </h2>
        );

    }

    if (!report) {

        return (
            <h2
                style={{
                    textAlign: "center",
                    marginTop: "100px"
                }}
            >
                Report Not Found
            </h2>
        );

    }

    return (

        <div
            style={{
                maxWidth: "1200px",
                margin: "40px auto",
                padding: "20px"
            }}
        >

            {/* Components will be connected next */}
            <ReportHeader
                company={report.company}
                role={report.role}
                overallScore={report.overall_score}
                date={report.created_at}
            />

        
            <OverallFeedback
                summary={report.summary}
                feedback={report.overall_feedback}
            />

            <div
                style={{
                    display: "grid",
                    gridTemplateColumns: "1fr 1fr",
                    gap: "25px",
                    marginBottom: "30px"
                }}
            >

                <StrongDomainsSection
                    domains={report.strong_domains}
                />

                <WeakDomainsSection
                    domains={report.weak_domains}
                />

            </div>


          <div
                style={{
                    display: "grid",
                    gridTemplateColumns: "1fr 1fr",
                    gap: "25px",
                    marginBottom: "30px"
                }}
            >

                <StrengthCard
                    strengths={report.strengths}
                />

                <WeaknessCard
                    weaknesses={report.weaknesses}
                />

            </div>
            <WeakSkillsSection
                skills={report.weak_skills}
            />

            
            <RecommendationCard
                recommendations={report.recommendations}
            />

            <HiringDecisionSection
                decision={report.hiring_decision}
                justification={report.hiring_justification}
            />


        </div>

    );

}

export default Report;

