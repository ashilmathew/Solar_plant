from fastapi import HTTPException, status

from app.repositories.analytics_repository import AnalyticsRepository


class AnalyticsService:

    def __init__(self):
        self.repository = AnalyticsRepository()

    async def get_device_analytics(self, device_id: str):

        telemetry = await self.repository.get_device_analytics(device_id)

        if not telemetry:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="No telemetry found"
            )

        powers = [
            t["electrical"]["power"]
            for t in telemetry
        ]

        voltages = [
            t["electrical"]["voltage"]
            for t in telemetry
        ]

        currents = [
            t["electrical"]["current"]
            for t in telemetry
        ]

        temperatures = [
            t["environment"]["temperature"]
            for t in telemetry
        ]

        latest = telemetry[-1]

        average_power = sum(powers) / len(powers)
        maximum_power = max(powers)
        minimum_power = min(powers)

        average_voltage = sum(voltages) / len(voltages)
        average_current = sum(currents) / len(currents)
        average_temperature = sum(temperatures) / len(temperatures)

        efficiency = (
            average_power / maximum_power * 100
            if maximum_power > 0
            else 0
        )

        return {

            "today_energy":
                latest["energy"]["today"],

            "total_energy":
                latest["energy"]["total"],

            "average_power":
                round(average_power, 2),

            "maximum_power":
                round(maximum_power, 2),

            "minimum_power":
                round(minimum_power, 2),

            "average_voltage":
                round(average_voltage, 2),

            "average_current":
                round(average_current, 2),

            "average_temperature":
                round(average_temperature, 2),

            "efficiency":
                round(efficiency, 2)
        }