import os
import json

from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def generate_questions( parsed_resume: dict,company: str,role: str,difficulty: str):

    prompt = f"""
You are an expert technical interviewer.

Candidate Resume:

{json.dumps(parsed_resume, indent=4)}

Company:
{company}

Role:
{role}

Difficulty:
{difficulty}

Generate exactly FIVE interview questions.

Rules:

1. Personalize questions using the resume.
2. Ask about projects.
3. Ask about technical skills.
4. Ask role-specific questions.
5. Return ONLY JSON.

Example:

{{
    "questions": [
        "...",
        "...",
        "...",
        "...",
        "..."
    ]
}}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
        config=types.GenerateContentConfig(
            response_mime_type="application/json"
        )
    )

    data = json.loads(response.text)

    return data["questions"]