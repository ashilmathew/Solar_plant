from bson import ObjectId

from app.database.database import telemetry_collection


class TelemetryRepository:

    async def create(self, telemetry):
        telemetry_dict = telemetry.model_dump()

        result = await telemetry_collection.insert_one(telemetry_dict)

        telemetry_dict["id"] = str(result.inserted_id)

        return telemetry_dict

    async def get_all(self):
        telemetry_list = []

        async for telemetry in telemetry_collection.find():
            telemetry["id"] = str(telemetry["_id"])
            del telemetry["_id"]
            telemetry_list.append(telemetry)

        return telemetry_list

    async def get_by_id(self, telemetry_id: str):
        telemetry = await telemetry_collection.find_one(
            {"_id": ObjectId(telemetry_id)}
        )

        if telemetry:
            telemetry["id"] = str(telemetry["_id"])
            del telemetry["_id"]

        return telemetry

    async def get_by_device(self, device_id: str):
        telemetry_list = []

        async for telemetry in telemetry_collection.find(
            {"device_id": device_id}
        ).sort("timestamp", -1):

            telemetry["id"] = str(telemetry["_id"])
            del telemetry["_id"]
            telemetry_list.append(telemetry)

        return telemetry_list

    async def get_latest(self, device_id: str):
        telemetry = await telemetry_collection.find_one(
            {"device_id": device_id},
            sort=[("timestamp", -1)]
        )

        if telemetry:
            telemetry["id"] = str(telemetry["_id"])
            del telemetry["_id"]

        return telemetry

    async def get_history(self, device_id: str, limit: int = 20):
        telemetry_list = []

        cursor = (
            telemetry_collection.find({"device_id": device_id})
            .sort("timestamp", -1)
            .limit(limit)
        )

        async for telemetry in cursor:
            telemetry["id"] = str(telemetry["_id"])
            del telemetry["_id"]
            telemetry_list.append(telemetry)

        return telemetry_list

    async def delete(self, telemetry_id: str):
        result = await telemetry_collection.delete_one(
            {"_id": ObjectId(telemetry_id)}
        )

        return result.deleted_count