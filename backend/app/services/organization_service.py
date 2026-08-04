from fastapi import HTTPException, status

from app.repositories.organization_repository import OrganizationRepository


class OrganizationService:

    def __init__(self):
        self.repository = OrganizationRepository()

    async def create(self, organization):
        return await self.repository.create(organization)

    async def get_all(self):
        return await self.repository.get_all()

    async def get_by_id(self, organization_id: str):
        organization = await self.repository.get_by_id(organization_id)

        if not organization:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Organization not found"
            )

        return organization

    async def update(self, organization_id: str, organization):
        updated = await self.repository.update(
            organization_id,
            organization
        )

        if not updated:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Organization not found"
            )

        return updated

    async def delete(self, organization_id: str):
        deleted = await self.repository.delete(organization_id)

        if deleted == 0:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Organization not found"
            )

        return {
            "message": "Organization deleted successfully"
        }