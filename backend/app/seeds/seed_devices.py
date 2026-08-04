import asyncio

from app.database.database import device_collection, plant_collection


async def seed():

    await device_collection.delete_many({})

    plants = await plant_collection.find().to_list(None)

    devices = []

    for plant in plants:

        devices.extend([
            {
                "name": "Inverter-01",
                "device_type": "Inverter",
                "serial_number": f"INV-{str(plant['_id'])[:6]}-01",
                "plant_id": str(plant["_id"]),
                "status": "ONLINE",
            },
            {
                "name": "Inverter-02",
                "device_type": "Inverter",
                "serial_number": f"INV-{str(plant['_id'])[:6]}-02",
                "plant_id": str(plant["_id"]),
                "status": "ONLINE",
            },
            {
                "name": "Energy Meter",
                "device_type": "Energy Meter",
                "serial_number": f"EM-{str(plant['_id'])[:6]}",
                "plant_id": str(plant["_id"]),
                "status": "ONLINE",
            },
            {
                "name": "Weather Station",
                "device_type": "Weather Station",
                "serial_number": f"WS-{str(plant['_id'])[:6]}",
                "plant_id": str(plant["_id"]),
                "status": "ONLINE",
            },
            {
                "name": "Battery Management System",
                "device_type": "Battery",
                "serial_number": f"BMS-{str(plant['_id'])[:6]}",
                "plant_id": str(plant["_id"]),
                "status": "ONLINE",
            },
        ])

    result = await device_collection.insert_many(devices)

    print(f"✅ {len(result.inserted_ids)} devices inserted.")


asyncio.run(seed())