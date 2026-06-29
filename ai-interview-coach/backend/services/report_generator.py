import json
from json import JSONDecodeError

from services.ai.ai_service import AIService
from services.prompts.report_prompt import create_report_prompt
from utils.logger import logger


ai = AIService()


def generate_interview_report(interview_data: dict):

    logger.info("Generating interview report")

    prompt = create_report_prompt(interview_data)

    response = ai.generate_report(prompt)

    print("\n================ AI RESPONSE ================\n")
    print(response)
    print("\n=============================================\n")

    try:

        report = json.loads(response)

        logger.info("Interview report generated successfully")

        return report

    except JSONDecodeError as e:

        print("JSON ERROR:", e)
        print("RAW RESPONSE:", response)

        raise Exception(f"AI returned invalid JSON: {response}")