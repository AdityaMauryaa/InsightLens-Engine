from typing import Any
import httpx
from app.config import settings
class WorldBankClient:
    def __init__(self) -> None:
        self.base_url = settings.world_bank_base_url
        self.timeout = settings.request_timeout

    async def fetch_data(
        self,country: str,
        indicator: str ,
        start_year: int | None = None,
        end_year: int | None = None,
    ) -> list[dict[str, Any]]:

        indicator_path = indicator
        url = (
            f"{self.base_url}/country/"
            f"{country}/indicator/{indicator_path}"
        )
        params = {
            "format": "json",
            "per_page": 100,
        }
        print(url)
        if start_year and end_year:
            params["date"] = f"{start_year}:{end_year}"

        async with httpx.AsyncClient(timeout=self.timeout) as client:
            response = await client.get(url, params=params)
            response.raise_for_status()
            
            return response.json()