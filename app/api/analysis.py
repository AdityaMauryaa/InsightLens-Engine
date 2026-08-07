from fastapi import APIRouter

from app.schemas import AnalysisRequest
from app.services.analysis_service import AnalysisService

router = APIRouter(
    prefix="/analysis",
    tags=["Analysis"],
)

analysis_service = AnalysisService()

@router.post("/")
async def analyze(request: AnalysisRequest):
    raw_result=await analysis_service.analyze(request)
    print(raw_result)
    return raw_result
