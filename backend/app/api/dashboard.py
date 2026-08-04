from fastapi import APIRouter

from app.schemas.dashboard import DashboardResponse
from app.services.dashboard_service import DashboardService

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"],
)

service = DashboardService()


@router.get(
    "/{plant_id}",
    response_model=DashboardResponse,
)
async def get_dashboard(plant_id: str):

    return await service.get_dashboard(plant_id)