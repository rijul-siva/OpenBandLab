import asyncio
# pyrefly: ignore [missing-import]
from bleak import BleakClient

ADDRESS = "44:27:F3:21:47:BC"

CHAR_51 = "00000051-0000-1000-8000-00805f9b34fb"


def handler(sender, data):
    print("\n===================")
    print("LEN :", len(data))
    print("HEX :", data.hex())

async def main():
    async with BleakClient(ADDRESS) as client:

        print("Connected")

        await client.start_notify(
            CHAR_51,
            handler
        )

        print("Listening on 51...")
        print("Press Ctrl+C to stop")

        while True:
            await asyncio.sleep(1)


if __name__ == "__main__":
    asyncio.run(main())