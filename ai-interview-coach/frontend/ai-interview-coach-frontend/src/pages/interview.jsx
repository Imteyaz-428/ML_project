import { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import api from "../services/api";

import QuestionCard from "../components/QuestionCard";
import AnswerBox from "../components/AnswerBox";
import FeedbackCard from "../components/FeedbackCard";

function Interview() {
    const [pageLoading, setPageLoading] = useState(true);
    const { id } = useParams();

    const [question, setQuestion] = useState(null);
    const [feedback, setFeedback] = useState(null);
    const [loading, setLoading] = useState(false);

    // ----------------------------
    // Load First / Next Question
    // ----------------------------
    async function loadQuestion() {

        try {
    
            const response = await api.get(`/question/next/${id}`);
    
            setQuestion(response.data);
    
        }
    
        catch (error) {
    
            console.log(error);
    
            if (error.response?.status === 404) {
    
                alert("Interview Completed!");
                setQuestion(null);
    
                return;
            }
    
            alert(
                error.response?.data?.detail ||
                "Unable to load question."
            );
    
        }
    
        finally {
    
            setPageLoading(false);
    
        }
    
    }

    // ----------------------------
    // Page Load
    // ----------------------------
    useEffect(() => {

        loadQuestion();

    }, [id]);

    // ----------------------------
    // Submit Answer
    // ----------------------------
    async function handleSubmit(answer) {

        if (!question) return;

        try {

            setLoading(true);

            const response = await api.post(
                `/question/submit/${question.id}`,
                {
                    user_answer: answer
                }
            );
            setFeedback(response.data.evaluation);

            if (response.data.completed) {

                alert("Interview Completed!");

            } else {

                setTimeout(() => {

                    setQuestion(response.data.next_question);

                    setFeedback(null);

                }, 3000);

            }

        }

        catch (error) {

            console.log(error);

            alert(
                error.response?.data?.detail ||
                "Failed to submit answer."
            );

        }

        finally {

            setLoading(false);

        }

    }

    // ----------------------------
    // Loading Screen
    // ----------------------------
    if (pageLoading) {

        return (
            <div
                style={{
                    textAlign: "center",
                    marginTop: "100px"
                }}
            >
                <h2>Loading Question...</h2>
            </div>
        );
    
    }
    if (!question) {

        return (
            <div
                style={{
                    textAlign: "center",
                    marginTop: "100px"
                }}
            >
                <h2>navigate(`/report/${id}`); 🎉</h2>
            </div>
        );
    
    }

    // ----------------------------
    // UI
    // ----------------------------
    return (

        <div
            style={{
                maxWidth: "1200px",
                margin: "40px auto",
                padding: "20px"
            }}
        >

            <QuestionCard

                company={question.company}

                role={question.role}

                currentQuestion={question.current_question}

                totalQuestions={question.total_questions}

                category={question.category}

                difficulty={question.difficulty_tag}

                question={question.question}

            />

            <AnswerBox

                loading={loading}

                onSubmit={handleSubmit}

            />

            <FeedbackCard

                feedback={feedback}

            />

        </div>

    );

}

export default Interview;