import asyncio
# pyrefly: ignore [missing-import]
from bleak import BleakClient
ADDRESS="44:27:F3:21:47:BC"

async def main():
    async with BleakClient(ADDRESS) as client:
        print(f"Connected to {client.address}")
        for service in client.services:
            print(f"service:{service.uuid}")
            for characteristic in service.characteristics:
                print(f"char:{characteristic.uuid}")
                print(f"charproperties:{characteristic.properties}")
                print()
if __name__=="__main__":
    asyncio.run(main()) 