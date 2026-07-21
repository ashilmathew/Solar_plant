from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.organization import OrganizationCreate, OrganizationResponse
from app.services.organization_service import OrganizationService
from app.schemas.organization import (
    OrganizationCreate,
    OrganizationUpdate,
    OrganizationResponse,
)

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
def create_organization(
    organization: OrganizationCreate,
    db: Session = Depends(get_db)
):
    return service.create(db, organization)
@router.get("/", response_model=list[OrganizationResponse])
def get_organizations(db: Session = Depends(get_db)):
    return service.get_all(db)


@router.get("/{organization_id}", response_model=OrganizationResponse)
def get_organization(
    organization_id: int,
    db: Session = Depends(get_db)
):
    return service.get_by_id(db, organization_id)


@router.put(
    "/{organization_id}",
    response_model=OrganizationResponse
)
def update_organization(
    organization_id: int,
    organization: OrganizationUpdate,
    db: Session = Depends(get_db)
):
    return service.update(db, organization_id, organization)


@router.delete("/{organization_id}")
def delete_organization(
    organization_id: int,
    db: Session = Depends(get_db)
):
    return service.delete(db, organization_id)