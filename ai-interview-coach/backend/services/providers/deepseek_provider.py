import os

from openai import OpenAI
from dotenv import load_dotenv

from services.providers.base_provider import BaseProvider

load_dotenv()


class DeepSeekProvider(BaseProvider):

    def __init__(self):

        self.client = OpenAI(
            api_key=os.getenv("DEEPSEEK_API_KEY"),
            base_url="https://api.deepseek.com"
        )

        self.model = "deepseek-v4-flash"

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