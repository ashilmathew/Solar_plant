from fastapi import APIRouter

from app.schemas.device import (
    DeviceCreate,
    DeviceResponse,
    DeviceUpdate
)
from app.services.device_service import DeviceService

router = APIRouter(
    prefix="/devices",
    tags=["Devices"]
)

service = DeviceService()


# Create Device
@router.post("/", response_model=DeviceResponse)
async def create_device(device: DeviceCreate):
    return await service.create(device)


# Get All Devices
@router.get("/", response_model=list[DeviceResponse])
async def get_all_devices():
    return await service.get_all()


# Get Device by ID
@router.get("/{device_id}", response_model=DeviceResponse)
async def get_device(device_id: str):
    return await service.get_by_id(device_id)


# Get All Devices of a Plant
@router.get("/plant/{plant_id}", response_model=list[DeviceResponse])
async def get_devices_by_plant(plant_id: str):
    return await service.get_by_plant(plant_id)


# Update Device
@router.put("/{device_id}", response_model=DeviceResponse)
async def update_device(device_id: str, device: DeviceUpdate):
    return await service.update(device_id, device)


# Delete Device
@router.delete("/{device_id}")
async def delete_device(device_id: str):
    return await service.delete(device_id)