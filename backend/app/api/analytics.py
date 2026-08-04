from fastapi import APIRouter

from app.schemas.analytics import AnalyticsResponse
from app.services.analytics_service import AnalyticsService

router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"]
)

service = AnalyticsService()


@router.get(
    "/device/{device_id}",
    response_model=AnalyticsResponse
)
async def get_device_analytics(device_id: str):

    return await service.get_device_analytics(device_id)