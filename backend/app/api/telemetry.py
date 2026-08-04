from fastapi import APIRouter

from app.schemas.telemetry import (
    TelemetryCreate,
    TelemetryResponse,
)
from app.services.telemetry_service import TelemetryService

router = APIRouter(
    prefix="/telemetry",
    tags=["Telemetry"]
)

service = TelemetryService()


# Create Telemetry
@router.post("/", response_model=TelemetryResponse)
async def create_telemetry(telemetry: TelemetryCreate):
    return await service.create(telemetry)


# Get All Telemetry
@router.get("/", response_model=list[TelemetryResponse])
async def get_all_telemetry():
    return await service.get_all()


# Get Telemetry by ID
@router.get("/{telemetry_id}", response_model=TelemetryResponse)
async def get_telemetry(telemetry_id: str):
    return await service.get_by_id(telemetry_id)


# Get All Telemetry for a Device
@router.get("/device/{device_id}", response_model=list[TelemetryResponse])
async def get_device_telemetry(device_id: str):
    return await service.get_by_device(device_id)


# Get Latest Telemetry for a Device
@router.get("/device/{device_id}/latest", response_model=TelemetryResponse)
async def get_latest_telemetry(device_id: str):
    return await service.get_latest(device_id)


# Get Telemetry History for a Device
@router.get("/device/{device_id}/history", response_model=list[TelemetryResponse])
async def get_telemetry_history(
    device_id: str,
    limit: int = 20
):
    return await service.get_history(device_id, limit)


# Delete Telemetry
@router.delete("/{telemetry_id}")
async def delete_telemetry(telemetry_id: str):
    return await service.delete(telemetry_id)