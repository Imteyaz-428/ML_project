import os

from dotenv import load_dotenv
from google import genai
from google.genai import types

from services.providers.base_provider import BaseProvider

load_dotenv()


class GeminiProvider(BaseProvider):

    def __init__(self):

        self.client = genai.Client(
            api_key=os.getenv("GEMINI_API_KEY")
        )

    def generate(self, prompt: str) -> str:

        response = self.client.models.generate_content(

            model="gemini-2.5-flash",

            contents=prompt,

            config=types.GenerateContentConfig(
                response_mime_type="application/json"
            )

        )

        return response.text