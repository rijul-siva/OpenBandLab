import asyncio
# pyrefly: ignore [missing-import]
from bleak import BleakClient

ADDRESS = "44:27:F3:21:47:BC"

CHAR = "00000052-0000-1000-8000-00805f9b34fb"

async def main():
    async with BleakClient(ADDRESS) as client:

        print("Connected")

        try:
            await client.write_gatt_char(
                CHAR,
                bytes([0x00]),
                response=False
            )

            print("Write sent")

        except Exception as e:
            print(e)

        await asyncio.sleep(10)

asyncio.run(main())