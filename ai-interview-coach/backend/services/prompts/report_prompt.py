import json

def create_report_prompt(interview_data: dict) -> str:

    questions = interview_data.get("questions", [])
    answered  = [q for q in questions if q.get("score") is not None]
    skipped   = len(questions) - len(answered)

    return f"""
You are a Senior Technical Interviewer with 15 years of FAANG hiring experience.
Evaluate the candidate below STRICTLY based on their actual answers only.

═══════════════════════════════════════
INTERVIEW DATA
═══════════════════════════════════════
{json.dumps(interview_data, indent=2)}

═══════════════════════════════════════
CONTEXT
═══════════════════════════════════════
- Total questions : {len(questions)}
- Answered        : {len(answered)}
- Skipped/Blank   : {skipped}
- Overall score   : {interview_data.get("overall_score", 0)} / 10
  (Pre-calculated by backend — do NOT change it)

═══════════════════════════════════════
STRICT RULES — FOLLOW ALL OF THEM
═══════════════════════════════════════
1. Return ONLY valid JSON. No markdown, no explanation, no extra text.
2. Do NOT change or recalculate overall_score — use it as-is.
3. Base EVERY claim strictly on what the candidate actually said.
   Never invent skills, knowledge, or answers not present in the data.
4. If the candidate skipped or gave a blank answer, treat it as a weakness.
5. Every bullet point: max 20 words, action-oriented, specific — no vague filler.
6. strong_domains and weak_domains must reflect actual interview evidence.
7. hiring_decision must follow the scoring guide below exactly.
8. weak_skills must list specific technical topics the candidate got wrong or skipped.

═══════════════════════════════════════
SCORING GUIDE — hiring_decision
═══════════════════════════════════════
"Strong Hire" → overall_score >= 8.0  AND no critical gaps
"Hire"        → overall_score >= 6.5  AND only minor gaps
"Maybe"       → overall_score >= 5.0  AND gaps are fixable with time
"No Hire"     → overall_score <  5.0  OR critical knowledge gaps present

═══════════════════════════════════════
YOUR TASKS
═══════════════════════════════════════
1. Write a 2–3 sentence professional recruiter-style summary.
2. Identify strongest technical domains with specific evidence from answers.
3. Identify weakest technical domains with specific gaps found.
4. List concrete strengths demonstrated during the interview.
5. List concrete weaknesses based on wrong/incomplete/skipped answers.
6. List specific, actionable improvement recommendations.
7. List weak skills — specific topics the candidate needs to study.
8. Make a final hiring decision with a one-line justification.

═══════════════════════════════════════
OUTPUT — return EXACTLY this JSON schema
═══════════════════════════════════════
{{
  "summary": "2-3 sentence professional recruiter summary",

  "overall_feedback":"One sentence describing overall interview performance",

  "strong_domains": [
    {{
      "domain": "e.g. Data Structures",
      "reason": "specific evidence from their answers"
    }}
  ],

  "weak_domains": [
    {{
      "domain": "e.g. System Design",
      "gap":    "specific gap found in their answers"
    }}
  ],

  "strengths": [
    "Concrete strength 1 — max 20 words",
    "Concrete strength 2 — max 20 words"
  ],

  "weaknesses": [
    "Concrete weakness 1 — max 20 words",
    "Concrete weakness 2 — max 20 words"
  ],

  "weak_skills": [
    "Specific topic or concept the candidate got wrong or skipped"
  ],

  "recommendations":[
   "Recommendation 1",
   "Recommendation 2",
   "Recommendation 3"
],

  "hiring_decision": "Strong Hire | Hire | Maybe | No Hire",

  "hiring_justification": "One-line reason tied directly to overall_score and gaps"
}}
"""