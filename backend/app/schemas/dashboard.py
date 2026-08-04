from pydantic import BaseModel
from datetime import datetime


class DashboardResponse(BaseModel):
    plant_name: str

    current_power: float
    today_energy: float

    temperature: float
    humidity: float

    weather_condition: str
    wind_speed: float

    running_inverters: int
    total_inverters: int

    battery_status: str
    plant_status: str

    last_updated: datetime