from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


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


class TelemetryBase(BaseModel):
    device_id: str
    timestamp: datetime

    electrical: ElectricalData
    energy: EnergyData
    environment: EnvironmentData

    status: str = "ONLINE"


class TelemetryCreate(TelemetryBase):
    pass


class TelemetryUpdate(BaseModel):
    electrical: Optional[ElectricalData] = None
    energy: Optional[EnergyData] = None
    environment: Optional[EnvironmentData] = None
    status: Optional[str] = None


class TelemetryResponse(TelemetryBase):
    id: str = Field(alias="id")

    model_config = {
        "populate_by_name": True
    }