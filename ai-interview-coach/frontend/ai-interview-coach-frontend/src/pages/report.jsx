import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";

import api from "../services/api";

import ReportHeader from "../components/ReportHeader";
import ScoreCards from "../components/ScoreCards";
import OverallFeedback from "../components/OverallFeedback";
import StrengthCard from "../components/StrengthCard";
import WeaknessCard from "../components/WeaknessCard";
import QuestionPerformance from "../components/QuestionPerformance";
import RecommendationCard from "../components/RecommendationCard";

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
                date={report.interview_date}
            />

            <ScoreCards

                technical={report.technical}

                communication={report.communication}

                confidence={report.confidence}

                problemSolving={report.problem_solving}
            />
            <OverallFeedback

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

                <StrengthCard
                    strengths={report.strengths}
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


                <WeaknessCard
                    weaknesses={report.weaknesses}
                />

            </div>

            <QuestionPerformance

                questions={report.questions}

            />
            <RecommendationCard

                recommendations={report.recommendations}

            />


        </div>

    );

}

export default Report;

