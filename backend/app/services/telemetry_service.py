from bson import ObjectId
from fastapi import HTTPException, status

from app.database.database import device_collection
from app.repositories.telemetry_repository import TelemetryRepository


class TelemetryService:

    def __init__(self):
        self.repository = TelemetryRepository()

    async def create(self, telemetry):

        device = await device_collection.find_one(
            {"_id": ObjectId(telemetry.device_id)}
        )

        if not device:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Device not found"
            )

        return await self.repository.create(telemetry)

    async def get_all(self):
        return await self.repository.get_all()

    async def get_by_id(self, telemetry_id: str):
        telemetry = await self.repository.get_by_id(telemetry_id)

        if not telemetry:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Telemetry not found"
            )

        return telemetry

    async def get_by_device(self, device_id: str):
        return await self.repository.get_by_device(device_id)

    async def get_latest(self, device_id: str):
        telemetry = await self.repository.get_latest(device_id)

        if not telemetry:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="No telemetry found"
            )

        return telemetry

    async def get_history(self, device_id: str, limit: int = 20):
        telemetry = await self.repository.get_history(device_id, limit)

        if not telemetry:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="No telemetry history found"
            )

        return telemetry

    async def delete(self, telemetry_id: str):
        deleted = await self.repository.delete(telemetry_id)

        if deleted == 0:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Telemetry not found"
            )

        return {
            "message": "Telemetry deleted successfully"
        }