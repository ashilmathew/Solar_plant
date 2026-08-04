from fastapi import APIRouter, status

from app.schemas.organization import (
    OrganizationCreate,
    OrganizationUpdate,
    OrganizationResponse,
)
from app.services.organization_service import OrganizationService

router = APIRouter(
    prefix="/organizations",
    tags=["Organizations"]
)

service = OrganizationService()


@router.post(
    "/",
    response_model=OrganizationResponse,
    status_code=status.HTTP_201_CREATED
)
async def create_organization(
    organization: OrganizationCreate,
):
    return await service.create(organization)


@router.get("/", response_model=list[OrganizationResponse])
async def get_organizations():
    return await service.get_all()


@router.get("/{organization_id}", response_model=OrganizationResponse)
async def get_organization(
    organization_id: str,
):
    return await service.get_by_id(organization_id)


@router.put(
    "/{organization_id}",
    response_model=OrganizationResponse
)
async def update_organization(
    organization_id: str,
    organization: OrganizationUpdate,
):
    return await service.update(organization_id, organization)


@router.delete("/{organization_id}")
async def delete_organization(
    organization_id: str,
):
    return await service.delete(organization_id)