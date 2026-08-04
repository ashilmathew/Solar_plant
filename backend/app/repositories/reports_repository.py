from bson import ObjectId

from app.database.database import (
    telemetry_collection,
    device_collection,
)


class ReportsRepository:

    async def get_device(self, device_id: str):

        return await device_collection.find_one(
            {
                "_id": ObjectId(device_id)
            }
        )

    async def get_report_data(self, device_id: str):

        telemetry = []

        cursor = telemetry_collection.find(
            {
                "device_id": device_id
            }
        )

        async for item in cursor:
            telemetry.append(item)

        return telemetry