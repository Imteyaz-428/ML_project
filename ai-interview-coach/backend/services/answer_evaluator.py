import os
import json

from dotenv import load_dotenv

from google import genai
from google.genai import types

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def evaluate_answer(
    question: str,
    user_answer: str,
    role: str,
    difficulty: str
):
    prompt = f"""
You are an experienced Technical Interviewer.

Evaluate the candidate's answer.

Question:
{question}

Candidate Answer:
{user_answer}

Role:
{role}

Difficulty:
{difficulty}

Instructions:

1. Score the answer between 0 and 10.
2. Explain why you gave this score.
3. Provide the ideal answer.
4. Mention the strengths.
5. Mention improvements.
6. Be constructive and professional.
7. Return ONLY valid JSON.
8. The "correct_answer" should be concise (maximum 200 words) and suitable for interview preparation.
9. Keep the feedback under 100 words.
10.Keep each strength to one sentence.
11.Keep each improvement to one sentence.

Example:

{{
    "score": 8,

    "feedback": "Good understanding of the topic but missed some important concepts.",

    "correct_answer": "Ideal answer goes here.",

    "strengths": [
        "Clear explanation",
        "Good technical understanding"
    ],

    "improvements": [
        "Mention more real-world examples",
        "Explain time complexity"
    ]
    "confidence": "Medium"
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