import asyncio

from app.core.security import hash_password
from app.database.database import user_collection


async def seed_admin():
    username = "admin"

    existing_user = await user_collection.find_one(
        {"username": username}
    )

    if existing_user:
        print("✅ SUPER_USER already exists.")
        return

    admin = {
        "username": "admin",
        "email": "admin@example.com",
        "hashed_password": hash_password("Admin@123"),
        "role": "SUPER_USER",
        "organization_id": None,
        "plant_id": None,
        "status": "ACTIVE",
    }

    result = await user_collection.insert_one(admin)

    print(f"✅ SUPER_USER created successfully.")
    print(f"User ID: {result.inserted_id}")
    print("Username: admin")
    print("Password: Admin@123")


if __name__ == "__main__":
    asyncio.run(seed_admin())