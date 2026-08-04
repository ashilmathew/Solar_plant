from bson import ObjectId
from fastapi import HTTPException, status

from app.database.database import organization_collection
from app.repositories.plant_repository import PlantRepository


class PlantService:

    def __init__(self):
        self.repository = PlantRepository()

    async def create(self, plant):

        organization = await organization_collection.find_one(
            {"_id": ObjectId(plant.organization_id)}
        )

        if not organization:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Organization not found"
            )

        return await self.repository.create(plant)

    async def get_all(self):
        return await self.repository.get_all()

    async def get_by_id(self, plant_id: str):

        plant = await self.repository.get_by_id(plant_id)

        if not plant:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Plant not found"
            )

        return plant

    async def get_by_organization(self, organization_id: str):

        organization = await organization_collection.find_one(
            {"_id": ObjectId(organization_id)}
        )

        if not organization:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Organization not found"
            )

        return await self.repository.get_by_organization(
            organization_id
        )

    async def update(self, plant_id: str, plant):

        updated = await self.repository.update(
            plant_id,
            plant
        )

        if not updated:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Plant not found"
            )

        return updated

    async def delete(self, plant_id: str):

        deleted = await self.repository.delete(plant_id)

        if deleted == 0:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Plant not found"
            )

        return {
            "message": "Plant deleted successfully"
        }