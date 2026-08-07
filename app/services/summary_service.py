from app.clients.llm_client import LLMClient
from app.prompts import SUMMARY_PROMPT
from app.schemas import IndicatorSeries

class SummaryService:
    def __init__(self) -> None:
        self.client = LLMClient()

    async def generate_summary(
        self,
        raw_data: list[IndicatorSeries],
    ) -> str:

        prompt = self._build_prompt(raw_data)

        return await self.client.generate(prompt)

    def _build_prompt(
        self,
        raw_data: list[IndicatorSeries],
    ) -> str:

        return SUMMARY_PROMPT.format(
            data=raw_data,
        )