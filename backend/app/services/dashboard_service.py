from fastapi import HTTPException

from app.repositories.dashboard_repository import DashboardRepository


class DashboardService:

    def __init__(self):
        self.repository = DashboardRepository()

    async def get_dashboard(self, plant_id: str):

        dashboard = await self.repository.get_dashboard(plant_id)

        if dashboard is None:
            raise HTTPException(
                status_code=404,
                detail="Plant not found",
            )

        return dashboard