import json

from services.prompts.evaluation_prompt import answer_evaluator_prompts
from services.ai.ai_service import AIService


ai = AIService()


def evaluate_answer(
    question: str,
    user_answer: str,
    role: str,
    difficulty: str,
):

    prompt = answer_evaluator_prompts(
        question,
        user_answer,
        role,
        difficulty,
    )

    response = ai.evaluate_answer(prompt)

    return json.loads(response)
    