import asyncio

from app.database.database import organization_collection, plant_collection


async def seed():

    await plant_collection.delete_many({})

    organizations = await organization_collection.find().to_list(None)

    plants = []

    for org in organizations:

        if org["name"] == "SolarTech Energy":
            plants.extend([
                {
                    "name": "Kannur Solar Plant",
                    "location": "Kannur",
                    "capacity": 500,
                    "organization_id": str(org["_id"]),
                },
                {
                    "name": "Payyannur Solar Plant",
                    "location": "Payyannur",
                    "capacity": 250,
                    "organization_id": str(org["_id"]),
                },
            ])

        elif org["name"] == "Green Power Ltd":
            plants.extend([
                {
                    "name": "Kochi Solar Plant",
                    "location": "Kochi",
                    "capacity": 750,
                    "organization_id": str(org["_id"]),
                },
                {
                    "name": "Aluva Solar Plant",
                    "location": "Aluva",
                    "capacity": 400,
                    "organization_id": str(org["_id"]),
                },
            ])

        elif org["name"] == "SunRise Renewables":
            plants.extend([
                {
                    "name": "Calicut Solar Plant",
                    "location": "Kozhikode",
                    "capacity": 600,
                    "organization_id": str(org["_id"]),
                }
            ])

        elif org["name"] == "EcoVolt Energy":
            plants.extend([
                {
                    "name": "Trivandrum Solar Plant",
                    "location": "Thiruvananthapuram",
                    "capacity": 900,
                    "organization_id": str(org["_id"]),
                }
            ])

    result = await plant_collection.insert_many(plants)

    print(f"✅ {len(result.inserted_ids)} plants inserted.")


asyncio.run(seed())