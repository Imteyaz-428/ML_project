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
You are a Senior Technical Interviewer with 15 years of FAANG hiring experience.
A candidate has just completed a technical interview.

Interview Details:
{json.dumps(interview_data, indent=4)}

STRICT RULES:
1. The "overall_score" is already calculated by the backend. Do NOT change it.
2. Return ONLY valid JSON. No explanation, no markdown, no extra text.
3. Every bullet: max 20 words, action-oriented, specific — no vague statements.
4. Never invent answers or skills not present in the interview data.
5. Base everything strictly on what the candidate actually said in their answers.

YOUR TASKS:
1. Write a 2-3 sentence professional recruiter summary of the candidate.
2. Identify their strongest technical domains (e.g. ML, Backend, Frontend, DSA).
3. Identify their weakest technical domains with specific gaps.
4. List concrete strengths shown during the interview.
5. List concrete weaknesses shown during the interview.
6. List specific, actionable improvement recommendations.
7. Make a final hiring decision with a one-line justification.

SCORING GUIDE for hiring_decision:
- "Strong Hire"  → overall_score >= 80, no major gaps
- "Hire"         → overall_score >= 65, minor gaps only
- "Maybe"        → overall_score >= 50, fixable gaps
- "No Hire"      → overall_score < 50, or critical gaps present

Return EXACTLY this JSON schema, no extra keys:
{{
    "summary": "",
    "performance": "",
    "strong_domains": [
        {{
            "domain": "",
            "reason": ""
        }}
    ],
    "weak_domains": [
        {{
            "domain": "",
            "gap": ""
        }}
    ],
    "strengths": [],
    "weaknesses": [],
    "weak_skills": [],
    "recommendation": "",
    "hiring_decision": "",
    "hiring_justification": ""
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