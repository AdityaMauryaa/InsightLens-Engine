from app.clients.world_bank_client import WorldBankClient

from app.schemas import (
    Country,
    Indicator,
    IndicatorSeries,
    TimeSeriesPoint,
)
class RawDataService:

    def __init__(self) -> None:
        self.client = WorldBankClient()

    async def get_raw_data(
        self,
        country: str,
        indicator: str,
        start_year: int | None = None,
        end_year: int | None = None,
    ) -> IndicatorSeries:
        
        response = await self.client.fetch_data(
            country=country,
            indicator=indicator,
            start_year=start_year,
            end_year=end_year,
        )
        return self._parse_response(response)

    def _parse_response(
        self,
        response: list,
    ) -> IndicatorSeries:
        """
        Convert the World Bank API response into an IndicatorSeries.
        """

        if not isinstance(response, list):
            raise ValueError("Invalid World Bank response.")

        if len(response) != 2:
            raise ValueError("Invalid World Bank response.")

        _, records = response

        if not records:
            raise ValueError("No data found.")

        first_record = records[0]

        country = Country(
            code=first_record["countryiso3code"],
            name=first_record["country"]["value"],
        )

        indicator = Indicator(
            code=first_record["indicator"]["id"],
            name=first_record["indicator"]["value"],
        )

        data = [
            TimeSeriesPoint(
                year=int(record["date"]),
                value=record["value"],
            )
            for record in records
        ]

        return IndicatorSeries(
            country=country,
            indicator=indicator,
            data=data,
        )