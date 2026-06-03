import asyncio
from bleak import BleakClient

ADDRESS = "44:27:F3:21:47:BC"

CHAR_50 = "00000050-0000-1000-8000-00805f9b34fb"


async def main():
    async with BleakClient(ADDRESS) as client:

        print("Connected")

        value = await client.read_gatt_char(CHAR_50)

        print("Raw Bytes:")
        print(value)

        print("\nHex:")
        print(value.hex())


if __name__ == "__main__":
    asyncio.run(main())