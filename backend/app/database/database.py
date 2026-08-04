import os

from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient

load_dotenv()

MONGODB_URL = os.getenv("MONGODB_URL")
DATABASE_NAME = os.getenv("DATABASE_NAME")

client = AsyncIOMotorClient(MONGODB_URL)

db = client[DATABASE_NAME]

organization_collection = db.organizations
plant_collection = db.plants
device_collection = db.devices
telemetry_collection = db.telemetry
user_collection = db.users


async def create_indexes():
    await user_collection.create_index(
        "username",
        unique=True
    )

    await user_collection.create_index(
        "email",
        unique=True,
        sparse=True
    )