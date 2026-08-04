from bson import ObjectId

from app.database.database import device_collection


class DeviceRepository:

    async def create(self, device):
        device_dict = device.model_dump()

        result = await device_collection.insert_one(device_dict)

        device_dict["id"] = str(result.inserted_id)

        return device_dict

    async def get_all(self):
        devices = []

        async for device in device_collection.find():
            device["id"] = str(device["_id"])
            del device["_id"]
            devices.append(device)

        return devices

    async def get_by_id(self, device_id: str):
        device = await device_collection.find_one(
            {"_id": ObjectId(device_id)}
        )

        if device:
            device["id"] = str(device["_id"])
            del device["_id"]

        return device

    async def get_by_plant(self, plant_id: str):
        devices = []

        async for device in device_collection.find(
            {"plant_id": plant_id}
        ):
            device["id"] = str(device["_id"])
            del device["_id"]
            devices.append(device)

        return devices

    async def update(self, device_id: str, device):
        await device_collection.update_one(
            {"_id": ObjectId(device_id)},
            {"$set": device.model_dump(exclude_unset=True)}
        )

        return await self.get_by_id(device_id)

    async def delete(self, device_id: str):
        result = await device_collection.delete_one(
            {"_id": ObjectId(device_id)}
        )

        return result.deleted_count