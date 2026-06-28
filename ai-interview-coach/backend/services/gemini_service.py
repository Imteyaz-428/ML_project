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
You are a Senior Technical Recruiter with 15 years of FAANG-level hiring experience.
Your job is to extract and analyze every important detail from the resume below.

STRICT RULES:
1. Return ONLY valid JSON. No preamble, no markdown, no backticks.
2. Never invent details. If data is missing, return [] or "" or 0.
3. Every bullet: max 20 words, action-verb first, quantified where possible.
4. Summary: exactly 2-3 recruiter-voice sentences. No fluff.
5. Strengths, weaknesses, recommendations: exactly 5 each.
6. Projects: 3-5 achievement bullets per project (what was built + impact).
7. Be strict and realistic with scoring. Do not inflate scores.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SCORING WEIGHTS  (resume_score out of 100)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ATS friendliness          15%   — clean structure, parseable format
  Technical skills match    20%   — relevance + breadth of tech stack
  Project quality           20%   — depth, complexity, real-world impact
  Work experience           20%   — seniority, scope, measurable results
  Education                 10%   — institution tier, GPA, relevance
  Quantified achievements   10%   — numbers, percentages, scale mentioned
  Action verbs & keywords    5%   — strong verbs, role-relevant terms

ATS SUB-SCORES (each 0-100):
  skills      — breadth and relevance of technologies listed
  projects    — technical depth, measurability, real deployment
  experience  — seniority level, team scope, career progression
  education   — institution quality, GPA, degree relevance
  keywords    — density of role-relevant terms for ATS parsing
  formatting  — structure clarity, section ordering, readability

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
DOMAIN ANALYSIS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Evaluate the candidate across these domains:
  Backend, Frontend, Machine Learning, Data Science,
  DevOps/Cloud, DSA/Competitive Programming, Mobile, Security

For each domain the candidate shows evidence of:
  - Rate it 0-100 based on skills + projects + experience combined
  - Only include domains where there is actual evidence (score > 0)
  - Identify their single best domain as "primary_domain"
  - Identify specific weak or missing skills per domain

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TARGET ROLE INFERENCE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
If no target role is stated on the resume:
  - Infer it from the strongest domain + skills + project work
  - Be specific: "ML Engineer" not just "Engineer"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CANDIDATE LEVEL INFERENCE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Based on total experience, project complexity, and skills:
  - "Fresher"        → 0 experience, projects only
  - "Junior"         → < 2 years experience
  - "Mid-Level"      → 2-5 years experience
  - "Senior"         → 5-10 years experience
  - "Staff/Lead"     → 10+ years or clear leadership evidence

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
RETURN THIS EXACT JSON SCHEMA:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{{
  "candidate_name": "",
  "target_role": "",
  "candidate_level": "",
  "primary_domain": "",
  "resume_score": 0,

  "ats_score": {{
    "skills": 0,
    "projects": 0,
    "experience": 0,
    "education": 0,
    "keywords": 0,
    "formatting": 0
  }},

  "summary": "",

  "domain_scores": [
    {{
      "domain": "",
      "score": 0,
      "evidence": "",
      "missing_skills": []
    }}
  ],

  "skills": [],
  "missing_skills": [],

  "strengths": [],
  "weaknesses": [],
  "recommendations": [],

  "projects": [
    {{
      "name": "",
      "description": [],
      "technologies": [],
      "impact": ""
    }}
  ],

  "experience": [
    {{
      "company": "",
      "role": "",
      "duration": "",
      "description": []
    }}
  ],

  "education": [
    {{
      "degree": "",
      "institution": "",
      "performance": "",
      "year_of_passing": ""
    }}
  ],

  "certifications": [],

  "achievements": []
}}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
FIELD GUIDE:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
candidate_level  → "Fresher" / "Junior" / "Mid-Level" / "Senior" / "Staff/Lead"
primary_domain   → single best domain e.g. "Machine Learning"
domain_scores    → only domains with actual evidence (score > 0)
  .evidence      → one sentence: what proves this domain (e.g. "3 ML projects + Scikit-learn + internship")
  .missing_skills→ what they need to strengthen this domain
projects
  .impact        → one line: measurable outcome or deployment context
missing_skills   → global list: what the candidate needs for their target role
certifications   → list of certs if mentioned, else []
achievements     → LeetCode ratings, hackathon wins, publications, awards — else []

RESUME:
{resume_text}
"""

   

    response = client.models.generate_content(model="gemini-2.5-flash",contents=prompt,config=types.GenerateContentConfig(response_mime_type="application/json"),)
    return json.loads(response.text)