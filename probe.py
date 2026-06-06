import asyncio
from bleak import BleakClient

ADDRESS = "44:27:F3:21:47:BC"

def cb(sender, data):
    print()
    print("NOTIFY")
    print("HANDLE:", sender)
    print("HEX:", data.hex())

async def main():
    async with BleakClient(ADDRESS) as client:

        print("Connected")

        for service in client.services:
            for char in service.characteristics:

                if "notify" in str(char.properties):

                    print("Subscribing:", char.uuid)

                    try:
                        await client.start_notify(char.uuid, cb)
                    except Exception as e:
                        print("Fail:", e)

        await asyncio.sleep(60)

asyncio.run(main())