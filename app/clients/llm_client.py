from groq import AsyncGroq

from app.config import settings

class LLMClient:

    def __init__(self) -> None:
        self.client = AsyncGroq(
            api_key=settings.groq_api_key,
        )

        self.model=settings.groq_model

    async def generate(
        self,
        prompt: str,
    ) -> str:

        response = await self.client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            temperature=0.2,
        )

        return response.choices[0].message.content