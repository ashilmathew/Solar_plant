from pydantic import BaseModel


class AnalyticsResponse(BaseModel):
    today_energy: float
    total_energy: float

    average_power: float
    maximum_power: float
    minimum_power: float

    average_voltage: float
    average_current: float

    average_temperature: float

    efficiency: float