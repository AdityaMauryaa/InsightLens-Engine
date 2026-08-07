from pydantic import BaseModel
from typing import List, Optional
# Common Models
class Country(BaseModel):
    code: str
    name: str
class Indicator(BaseModel):
    code: str
    name: str
class TimeSeriesPoint(BaseModel):
    year: int
    value: Optional[float] = None
class IndicatorSeries(BaseModel):
    country: Country
    indicator: Indicator
    data: List[TimeSeriesPoint]

class Summary(BaseModel):
    content: str


# ----------------------------
# Request Schemas
# ----------------------------

class AnalysisRequest(BaseModel):
    country: str
    indicators: List[str]
    start_year: Optional[int] = None
    end_year: Optional[int] = None


class ComparisonRequest(BaseModel):
    countries: List[str]          # Exactly 2 for Version 1
    indicators: List[str]
    start_year: Optional[int] = None
    end_year: Optional[int] = None

# Response Schemas
class AnalysisResponse(BaseModel):
    raw_data: List[IndicatorSeries]
    summary: str

class ComparisonResponse(BaseModel):
    raw_data: List[IndicatorSeries]
    summary: str