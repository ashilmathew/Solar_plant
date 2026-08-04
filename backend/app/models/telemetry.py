from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class ElectricalData(BaseModel):
    voltage: float
    current: float
    frequency: float
    power: float
    power_factor: float


class EnergyData(BaseModel):
    today: float
    total: float


class EnvironmentData(BaseModel):
    temperature: float
    humidity: Optional[float] = None


class Telemetry(BaseModel):
    device_id: str
    timestamp: datetime

    electrical: ElectricalData
    energy: EnergyData
    environment: EnvironmentData

    status: str = "ONLINE"