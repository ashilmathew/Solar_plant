from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.repositories.organization_repository import OrganizationRepository
from app.schemas.organization import (
    OrganizationCreate,
    OrganizationUpdate,
)


class OrganizationService:

    def __init__(self):
        self.repository = OrganizationRepository()

    def create(self, db: Session, organization: OrganizationCreate):
        return self.repository.create(db, organization)

    def get_all(self, db: Session):
        return self.repository.get_all(db)

    def get_by_id(self, db: Session, organization_id: int):
        organization = self.repository.get_by_id(db, organization_id)

        if not organization:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Organization not found"
            )

        return organization

    def update(
        self,
        db: Session,
        organization_id: int,
        organization: OrganizationUpdate
    ):
        db_org = self.repository.update(db, organization_id, organization)

        if not db_org:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Organization not found"
            )

        return db_org

    def delete(self, db: Session, organization_id: int):
        db_org = self.repository.delete(db, organization_id)

        if not db_org:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Organization not found"
            )

        return {"message": "Organization deleted successfully"}