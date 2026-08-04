import asyncio

from app.core.security import hash_password
from app.database.database import organization_collection, plant_collection, user_collection


async def seed():

    organizations = await organization_collection.find().to_list(None)
    plants = await plant_collection.find().to_list(None)

    # Delete all users except the SUPER_USER
    await user_collection.delete_many(
        {
            "role": {
                "$ne": "SUPER_USER"
            }
        }
    )

    users = []

    # Organization Users
    for org in organizations:

        username = (
            org["name"]
            .lower()
            .replace(" ", "_")
            .replace(".", "")
        )

        users.append(
            {
                "username": f"{username}_admin",
                "email": f"{username}@solar.com",
                "hashed_password": hash_password("Admin@123"),
                "role": "ORGANIZATION",
                "organization_id": str(org["_id"]),
                "plant_id": None,
                "status": "ACTIVE",
            }
        )

    # Plant Users
    for plant in plants:

        username = (
            plant["name"]
            .lower()
            .replace(" ", "_")
            .replace(".", "")
        )

        users.append(
            {
                "username": f"{username}_user",
                "email": f"{username}@solar.com",
                "hashed_password": hash_password("Plant@123"),
                "role": "PLANT",
                "organization_id": plant["organization_id"],
                "plant_id": str(plant["_id"]),
                "status": "ACTIVE",
            }
        )

    result = await user_collection.insert_many(users)

    print("=" * 50)
    print(f"✅ {len(result.inserted_ids)} users inserted.")
    print("=" * 50)


asyncio.run(seed())