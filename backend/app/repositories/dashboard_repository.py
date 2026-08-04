from bson import ObjectId
from datetime import datetime

from app.database.database import (
    plant_collection,
    device_collection,
    telemetry_collection,
)


class DashboardRepository:

    async def get_dashboard(self, plant_id: str):

        plant = await plant_collection.find_one(
            {"_id": ObjectId(plant_id)}
        )

        if not plant:
            return None

        devices = await device_collection.find(
            {"plant_id": plant_id}
        ).to_list(None)

        total_power = 0
        total_energy = 0
        total_temp = 0
        total_humidity = 0

        running = 0
        latest_time = None

        for device in devices:

            telemetry = await telemetry_collection.find_one(
                {"device_id": str(device["_id"])},
                sort=[("timestamp", -1)],
            )

            if telemetry is None:
                continue

            electrical = telemetry.get("electrical", {})
            energy = telemetry.get("energy", {})
            environment = telemetry.get("environment", {})

            total_power += electrical.get("power", 0)
            total_energy += energy.get("today", 0)
            total_temp += environment.get("temperature", 0)
            total_humidity += environment.get("humidity", 0)

            if telemetry.get("status") == "ONLINE":
                running += 1

            ts = telemetry.get("timestamp")

            if ts:
                if latest_time is None or ts > latest_time:
                    latest_time = ts

        device_count = len(devices)

        return {
            "plant_name": plant["name"],

            "current_power": round(total_power, 2),

            "today_energy": round(total_energy, 2),

            "temperature": round(
                total_temp / device_count, 2
            ) if device_count else 0,

            "humidity": round(
                total_humidity / device_count, 2
            ) if device_count else 0,

            "weather_condition": "Sunny",

            "wind_speed": 0,

            "running_inverters": running,

            "total_inverters": device_count,

            "battery_status": "Healthy",

            "plant_status": "ONLINE" if running else "OFFLINE",

            "last_updated": latest_time or datetime.utcnow(),
        }