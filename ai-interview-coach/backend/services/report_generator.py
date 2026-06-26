import os
import json

from dotenv import load_dotenv

from google import genai
from google.genai import types

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def generate_interview_report(interview_data: dict):

    prompt = f"""
You are a Senior Technical Interviewer.

A candidate has completed an interview.

Interview Details:

{json.dumps(interview_data, indent=4)}

The "overall_score" has already been calculated by the backend.
Do NOT recalculate it.

Your task is to analyze the candidate's overall performance.

Instructions:

1. Analyze the interview based on all questions.
2. Identify overall strengths.
3. Identify overall weaknesses.
4. Give practical recommendations for improvement.
5. Decide whether the candidate should be hired.
6. Keep recommendations concise.
7. Return ONLY valid JSON.

Return exactly this format:

{{
    "performance": "",

    "strengths": [],

    "weaknesses": [],

    "recommendation": "",

    "hiring_decision": ""
}}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
        config=types.GenerateContentConfig(
            response_mime_type="application/json"
        )
    )

    return json.loads(response.text)