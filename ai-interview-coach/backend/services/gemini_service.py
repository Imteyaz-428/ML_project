import os
import json
from google.genai import types
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def extract_resume_information(resume_text: str):

    prompt = f"""
You are an AI Resume Analyzer.

Analyze the following resume.

Extract:

1. Skills
2. Projects
3. Education
4. Experience
5. Certifications

Return ONLY valid JSON.

Example:

{{
    "skills": [],
    "projects": [],
    "education": "",
    "experience": "",
    "certifications": []
}}

Resume:

{resume_text}
"""

   

    response = client.models.generate_content(model="gemini-2.5-flash",contents=prompt,config=types.GenerateContentConfig(response_mime_type="application/json"),)
    return json.loads(response.text)