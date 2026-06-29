import json
from services.ai.ai_service import AIService
from services.prompts.question_prompt import build_question_prompt

# flow :-   question_generator -> question_prompt -> ai_services -> gimini_provider -> gemini_api

def generate_questions( parsed_resume: dict,company: str,role: str,difficulty: str,interview_type, no_of_questions):

    prompt = build_question_prompt(
    parsed_resume=parsed_resume,
    company=company,
    role=role,
    difficulty=difficulty,
    interview_type=interview_type,
    no_of_questions=no_of_questions)

    
    
    ai = AIService()

    response = ai.generate_questions(prompt)

    data = json.loads(response)

    return data