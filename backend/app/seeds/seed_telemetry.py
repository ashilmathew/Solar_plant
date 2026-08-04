import asyncio
import random
from datetime import datetime, timedelta

from app.database.database import device_collection, telemetry_collection


async def seed():

    await telemetry_collection.delete_many({})

    devices = await device_collection.find().to_list(None)

    telemetry = []

    now = datetime.utcnow()

    for device in devices:

        total_energy = random.uniform(10000, 30000)

        # Generate 100 readings per device
        for i in range(100):

            voltage = round(random.uniform(220, 240), 2)
            current = round(random.uniform(5, 25), 2)
            power = round((voltage * current) / 1000, 2)
            frequency = round(random.uniform(49.8, 50.2), 2)
            power_factor = round(random.uniform(0.95, 1.00), 2)

            today_energy = round(random.uniform(20, 150), 2)
            total_energy += round(random.uniform(0.05, 0.50), 2)

            temperature = round(random.uniform(28, 42), 2)
            humidity = round(random.uniform(45, 90), 2)

            telemetry.append(
                {
                    "device_id": str(device["_id"]),

                    "electrical": {
                        "voltage": voltage,
                        "current": current,
                        "frequency": frequency,
                        "power": power,
                        "power_factor": power_factor,
                    },

                    "energy": {
                        "today": today_energy,
                        "total": round(total_energy, 2),
                    },

                    "environment": {
                        "temperature": temperature,
                        "humidity": humidity,
                    },

                    "status": random.choice(
                        [
                            "ONLINE",
                            "ONLINE",
                            "ONLINE",
                            "ONLINE",
                            "WARNING",
                            "OFFLINE",
                        ]
                    ),

                    "timestamp": now - timedelta(minutes=5 * (100 - i)),
                }
            )

    result = await telemetry_collection.insert_many(telemetry)

    print("=" * 60)
    print(f"✅ {len(result.inserted_ids)} telemetry records inserted.")
    print("=" * 60)


asyncio.run(seed())