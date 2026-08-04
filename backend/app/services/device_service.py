from bson import ObjectId
from fastapi import HTTPException, status

from app.database.database import plant_collection
from app.repositories.device_repository import DeviceRepository


class DeviceService:

    def __init__(self):
        self.repository = DeviceRepository()

    async def create(self, device):

        plant = await plant_collection.find_one(
            {"_id": ObjectId(device.plant_id)}
        )

        if not plant:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Plant not found"
            )

        return await self.repository.create(device)

    async def get_all(self):
        return await self.repository.get_all()

    async def get_by_id(self, device_id: str):
        device = await self.repository.get_by_id(device_id)

        if not device:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Device not found"
            )

        return device

    async def get_by_plant(self, plant_id: str):

        plant = await plant_collection.find_one(
            {"_id": ObjectId(plant_id)}
        )

        if not plant:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Plant not found"
            )

        return await self.repository.get_by_plant(plant_id)

    async def update(self, device_id: str, device):
        updated = await self.repository.update(device_id, device)

        if not updated:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Device not found"
            )

        return updated

    async def delete(self, device_id: str):
        deleted = await self.repository.delete(device_id)

        if deleted == 0:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Device not found"
            )

        return {
            "message": "Device deleted successfully"
        }