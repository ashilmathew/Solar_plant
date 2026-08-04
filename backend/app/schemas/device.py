from typing import Optional

from pydantic import BaseModel, Field


class DeviceBase(BaseModel):
    plant_id: str
    name: str
    device_type: str
    manufacturer: Optional[str] = None
    model: Optional[str] = None
    serial_number: str
    firmware_version: Optional[str] = None
    installation_date: Optional[str] = None
    status: str = "ONLINE"


class DeviceCreate(DeviceBase):
    pass


class DeviceUpdate(BaseModel):
    plant_id: Optional[str] = None
    name: Optional[str] = None
    device_type: Optional[str] = None
    manufacturer: Optional[str] = None
    model: Optional[str] = None
    serial_number: Optional[str] = None
    firmware_version: Optional[str] = None
    installation_date: Optional[str] = None
    status: Optional[str] = None


class DeviceResponse(DeviceBase):
    id: str = Field(alias="id")

    model_config = {
        "populate_by_name": True
    }