from typing import Optional

from pydantic import BaseModel, Field


class PlantBase(BaseModel):
    organization_id: str
    name: str
    capacity: float
    location: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    commissioning_date: Optional[str] = None
    status: str = "ACTIVE"


class PlantCreate(PlantBase):
    pass


class PlantUpdate(BaseModel):
    organization_id: Optional[str] = None
    name: Optional[str] = None
    capacity: Optional[float] = None
    location: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    commissioning_date: Optional[str] = None
    status: Optional[str] = None


class PlantResponse(PlantBase):
    id: str = Field(alias="id")

    model_config = {
        "populate_by_name": True
    }