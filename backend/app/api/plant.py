from fastapi import APIRouter

from app.schemas.plant import PlantCreate, PlantResponse, PlantUpdate
from app.services.plant_service import PlantService

router = APIRouter(
    prefix="/plants",
    tags=["Plants"]
)

service = PlantService()


@router.post("/", response_model=PlantResponse)
async def create_plant(plant: PlantCreate):
    return await service.create(plant)


@router.get("/", response_model=list[PlantResponse])
async def get_all_plants():
    return await service.get_all()


# NEW ENDPOINT
@router.get(
    "/organization/{organization_id}",
    response_model=list[PlantResponse]
)
async def get_plants_by_organization(
    organization_id: str,
):
    return await service.get_by_organization(
        organization_id
    )


@router.get("/{plant_id}", response_model=PlantResponse)
async def get_plant(plant_id: str):
    return await service.get_by_id(plant_id)


@router.put("/{plant_id}", response_model=PlantResponse)
async def update_plant(
    plant_id: str,
    plant: PlantUpdate
):
    return await service.update(
        plant_id,
        plant
    )


@router.delete("/{plant_id}")
async def delete_plant(plant_id: str):
    return await service.delete(plant_id)