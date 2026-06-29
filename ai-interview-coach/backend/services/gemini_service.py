import json

from services.ai.ai_service import AIService
from services.prompts.resume_prompt import build_resume_prompt


ai = AIService()


def extract_resume_information(resume_text: str):

    prompt = build_resume_prompt(resume_text)

    response = ai.analyze_resume(prompt)

    return json.loads(response)