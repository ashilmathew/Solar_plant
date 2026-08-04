import asyncio
import os
import sys

# Add backend folder to Python path
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.insert(0, BASE_DIR)

from app.database.database import organization_collection


organizations = [
    {
        "name": "SolarTech Energy",
        "location": "Kannur, Kerala",
        "contact_email": "info@solartech.com",
        "contact_phone": "+91 9876543210",
    },
    {
        "name": "Green Power Ltd",
        "location": "Kochi, Kerala",
        "contact_email": "contact@greenpower.com",
        "contact_phone": "+91 9876543211",
    },
    {
        "name": "SunRise Renewables",
        "location": "Kozhikode, Kerala",
        "contact_email": "admin@sunrise.com",
        "contact_phone": "+91 9876543212",
    },
    {
        "name": "EcoVolt Energy",
        "location": "Thiruvananthapuram, Kerala",
        "contact_email": "support@ecovolt.com",
        "contact_phone": "+91 9876543213",
    },
]


async def seed():
    print("Deleting existing organizations...")
    await organization_collection.delete_many({})

    print("Inserting organizations...")
    result = await organization_collection.insert_many(organizations)

    print("=" * 50)
    print(f"✅ Successfully inserted {len(result.inserted_ids)} organizations")
    print("=" * 50)

    for org_id in result.inserted_ids:
        print(org_id)


if __name__ == "__main__":
    asyncio.run(seed())