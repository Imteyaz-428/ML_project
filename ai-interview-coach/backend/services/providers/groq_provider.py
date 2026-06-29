import os

from groq import Groq
from dotenv import load_dotenv

from services.providers.base_provider import BaseProvider

load_dotenv()


class GroqProvider(BaseProvider):

    def __init__(self):

        self.client = Groq(
            api_key=os.getenv("GROQ_API_KEY")
        )

        # We'll make this configurable later
        self.model = "llama-3.3-70b-versatile"

    def generate(self, prompt: str) -> str:

        response = self.client.chat.completions.create(

            model=self.model,

            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],

            temperature=0.3,

            response_format={
                "type": "json_object"
            }

        )

        return response.choices[0].message.content