from app.database.database import telemetry_collection


class AnalyticsRepository:

    async def get_device_analytics(self, device_id: str):

        telemetry = []

        cursor = telemetry_collection.find(
            {"device_id": device_id}
        )

        async for item in cursor:
            telemetry.append(item)

        return telemetry