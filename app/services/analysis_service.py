import asyncio

from app.schemas import (
    AnalysisRequest,
    AnalysisResponse,
)
from app.services.summary_service import SummaryService
from app.services.raw_data_service import RawDataService

class AnalysisService:
    def __init__(self) -> None:
        self.raw_data_service = RawDataService()
        self.summary_service = SummaryService()

    async def analyze(
        self,
        request: AnalysisRequest,
    ) -> AnalysisResponse:

        raw_data = await asyncio.gather(
            *[
                self.raw_data_service.get_raw_data(
                    country=request.country,
                    indicator=indicator,
                    start_year=request.start_year,
                    end_year=request.end_year,
                )
                for indicator in request.indicators
            ]
        )

        return AnalysisResponse(
            raw_data=raw_data,
            summary = await self.summary_service.generate_summary(raw_data)
        )