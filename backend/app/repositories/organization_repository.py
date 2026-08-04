from bson import ObjectId

from app.database.database import organization_collection


class OrganizationRepository:

    async def create(self, organization):
        organization_dict = organization.model_dump()

        result = await organization_collection.insert_one(organization_dict)

        organization_dict["id"] = str(result.inserted_id)

        return organization_dict

    async def get_all(self):
        organizations = []

        async for organization in organization_collection.find():
            organization["id"] = str(organization["_id"])
            del organization["_id"]
            organizations.append(organization)

        return organizations

    async def get_by_id(self, organization_id: str):

        organization = await organization_collection.find_one(
            {"_id": ObjectId(organization_id)}
        )

        if organization:
            organization["id"] = str(organization["_id"])
            del organization["_id"]

        return organization

    async def update(self, organization_id: str, organization):

        await organization_collection.update_one(
            {"_id": ObjectId(organization_id)},
            {"$set": organization.model_dump(exclude_unset=True)}
        )

        return await self.get_by_id(organization_id)

    async def delete(self, organization_id: str):

        result = await organization_collection.delete_one(
            {"_id": ObjectId(organization_id)}
        )

        return result.deleted_count