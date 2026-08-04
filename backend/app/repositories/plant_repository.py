from bson import ObjectId

from app.database.database import plant_collection


class PlantRepository:

    async def create(self, plant):
        plant_dict = plant.model_dump()

        result = await plant_collection.insert_one(plant_dict)

        plant_dict["id"] = str(result.inserted_id)

        return plant_dict

    async def get_all(self):
        plants = []

        async for plant in plant_collection.find():
            plant["id"] = str(plant["_id"])
            del plant["_id"]
            plants.append(plant)

        return plants

    async def get_by_id(self, plant_id: str):
        plant = await plant_collection.find_one(
            {"_id": ObjectId(plant_id)}
        )

        if plant:
            plant["id"] = str(plant["_id"])
            del plant["_id"]

        return plant

    async def get_by_organization(self, organization_id: str):
        plants = []

        async for plant in plant_collection.find(
            {"organization_id": organization_id}
        ):
            plant["id"] = str(plant["_id"])
            del plant["_id"]
            plants.append(plant)

        return plants

    async def update(self, plant_id: str, plant):
        await plant_collection.update_one(
            {"_id": ObjectId(plant_id)},
            {"$set": plant.model_dump(exclude_unset=True)}
        )

        return await self.get_by_id(plant_id)

    async def delete(self, plant_id: str):
        result = await plant_collection.delete_one(
            {"_id": ObjectId(plant_id)}
        )

        return result.deleted_count