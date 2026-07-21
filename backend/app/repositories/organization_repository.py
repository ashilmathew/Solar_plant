from sqlalchemy.orm import Session

from app.models.organization import Organization
from app.schemas.organization import OrganizationCreate, OrganizationUpdate


class OrganizationRepository:

    def create(self, db: Session, organization: OrganizationCreate):
        db_org = Organization(**organization.model_dump())

        db.add(db_org)
        db.commit()
        db.refresh(db_org)

        return db_org

    def get_all(self, db: Session):
        return db.query(Organization).all()

    def get_by_id(self, db: Session, organization_id: int):
        return (
            db.query(Organization)
            .filter(Organization.id == organization_id)
            .first()
        )

    def update(
        self,
        db: Session,
        organization_id: int,
        organization: OrganizationUpdate
    ):
        db_org = self.get_by_id(db, organization_id)

        if not db_org:
            return None

        update_data = organization.model_dump(exclude_unset=True)

        for key, value in update_data.items():
            setattr(db_org, key, value)

        db.commit()
        db.refresh(db_org)

        return db_org

    def delete(self, db: Session, organization_id: int):
        db_org = self.get_by_id(db, organization_id)

        if not db_org:
            return None

        db.delete(db_org)
        db.commit()

        return db_org