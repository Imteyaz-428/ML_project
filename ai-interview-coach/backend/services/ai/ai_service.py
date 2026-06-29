from services.providers.gemini_provider import GeminiProvider
from services.providers.groq_provider import GroqProvider
from services.providers.deepseek_provider import DeepSeekProvider
from utils.retry import retry_request

from utils.logger import logger

from config import (
    RESUME_PROVIDERS,
    QUESTION_PROVIDERS,
    EVALUATION_PROVIDERS,
    REPORT_PROVIDERS
)


class AIService:

    def __init__(self):

        self.providers = {
            "gemini": GeminiProvider(),
            "groq": GroqProvider(),
            "deepseek": DeepSeekProvider(),
        }

    def _provider(self, provider_name):

        provider = self.providers.get(provider_name)

        if provider is None:
            raise ValueError(
                f"Unknown provider: {provider_name}"
            )

        return provider

    def _generate_with_fallback(
        self,
        providers,
        prompt
    ):

        for provider_name in providers:

            try:

                logger.info(f"Using AI Provider: {provider_name}")

                response = retry_request(
                    self._provider(provider_name).generate,
                    prompt
                )

                logger.info(
                    f"{provider_name} generated response successfully"
                )

                return response

            except Exception as e:

                logger.warning(
                    f"{provider_name} failed: {e}"
                )

        logger.error("All AI providers failed.")

        raise Exception("All providers failed.")

    # Resume
    def analyze_resume(self, prompt):

        return self._generate_with_fallback(
            RESUME_PROVIDERS,
            prompt
        )

    # Questions
    def generate_questions(self, prompt):

        return self._generate_with_fallback(
            QUESTION_PROVIDERS,
            prompt
        )

    # Evaluation
    def evaluate_answer(self, prompt):

        return self._generate_with_fallback(
            EVALUATION_PROVIDERS,
            prompt
        )

    # Report
    def generate_report(self, prompt):

        return self._generate_with_fallback(
            REPORT_PROVIDERS,
            prompt
        )