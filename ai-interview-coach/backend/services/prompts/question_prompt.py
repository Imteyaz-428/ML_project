import json



def build_question_prompt(parsed_resume: dict,company: str,role: str,difficulty: str, interview_type: str, no_of_questions: int,):

    return   f"""
You are a Senior Technical Interviewer at {company} with 15 years of hiring experience.
You are conducting a {difficulty}-level interview for the role of {role}.

Candidate Resume Analysis:
{json.dumps(parsed_resume, indent=4)}

YOUR GOAL:
Generate a complete, personalized interview question set that:
- Is tailored to THIS candidate's actual projects, skills, and experience level
- Matches the {difficulty} difficulty bar
- Covers all important technical areas for the {role} role
- Includes a mix of question types (see categories below)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
DIFFICULTY GUIDE  
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Easy   → Fresher/Junior level. Basics, definitions, simple project walkthroughs.
Medium → Mid-level. Design decisions, tradeoffs, optimization, debugging.
Hard   → Senior level. System design at scale, architecture, deep internals.

Current difficulty: {difficulty}
Candidate level from resume:
{parsed_resume.get("candidate_level","Unknown")}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION CATEGORIES  
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. project_deep_dive    → Ask about a specific project from the resume.
                          Probe: architecture decisions, challenges, what they would change.
2. technical_concept    → Core concept from their strongest skill/domain.
                          Probe: how it works internally, not just definitions.
3. problem_solving      → DSA or coding logic question relevant to the role.
                          Match difficulty level strictly.
4. system_design        → Design a system relevant to the role and company.
                          Scale to difficulty (Easy = simple API, Hard = distributed system).
5. behavioral           → Situation-based question tied to something in their resume.
                          Use STAR format expectation.
6. role_specific        → A question only someone in {role} at {company} would face.
                          Use company domain knowledge if possible.
7. weakness_probe       → Ask about a skill gap visible in the resume (from missing_skills).
                          Goal: see how self-aware and growth-oriented the candidate is.



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STRICT RULES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Generate exactly {no_of_questions} questions.
    Distribute them across the categories naturally.
    Prioritize:
    - Project Deep Dive
    - Technical Concepts
    - Role Specific
    Repeat categories when necessary.
    Avoid duplicate questions.
2. Every question MUST reference something specific from the resume (project name, skill, or achievement).
3. Do NOT ask generic questions like "Tell me about yourself" or "What are your strengths?".
4. difficulty must strictly match — do not mix Easy questions in a Hard interview.
5. follow_up must be a real probing question, not a rephrasing of the main question.
6. expected_answer_points must be concrete things the candidate should mention — not vague.
7. Return ONLY valid JSON. No explanation, no markdown.
8. For product based company , you can generate dsa question also.
9. INTERVIEW TYPE :-
Technical
→ 80% technical, 20% behavioral
Behavioral
→ 80% behavioral, 20% technical
HR
→ Focus on communication, teamwork,
career motivation, conflict resolution.
Mixed
→ Balanced distribution.
Selected Interview Type:
{interview_type}
10. If the resume contains no projects,
replace project_deep_dive with
skill_deep_dive using the strongest skill.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
RETURN EXACTLY THIS JSON SCHEMA:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{{
  "interview_meta": {{
    "company": "{company}",
    "role": "{role}",
    "difficulty": "{difficulty}",
    "candidate_name": "",
  }},
  "questions": [
    {{
      "id": 1,
      "category": "",
      "question": "",
      "follow_up": "",
      "expected_answer_points": [],
      "time_limit_minutes": 0,
      "difficulty_tag": ""
    }}
  ]
}}

FIELD GUIDE:
  category              → one of the 7 categories listed above
  question              → the actual question to ask the candidate
  follow_up             → a deeper probing question to ask after their answer
  expected_answer_points→ 3-5 specific points a good answer should cover
  difficulty_tag        → "Easy" / "Medium" / "Hard"

"""

