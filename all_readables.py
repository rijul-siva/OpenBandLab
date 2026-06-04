import asyncio
from bleak import BleakClient

ADDRESS = "44:27:F3:21:47:BC"


async def main():
    async with BleakClient(ADDRESS) as client:

        print(f"Connected: {client.is_connected}\n")

        for service in client.services:
            print(f"\nSERVICE: {service.uuid}")

            for char in service.characteristics:

                if "read" not in char.properties:
                    continue

                print(f"\nCHAR: {char.uuid}")

                try:
                    data = await client.read_gatt_char(char.uuid)

                    print(f"LEN : {len(data)}")
                    print(f"HEX : {data.hex()}")

                    try:
                        print(f"TEXT: {data.decode('utf-8')}")
                    except:
                        pass

                except Exception as e:
                    print(f"READ FAILED: {e}")


if __name__ == "__main__":
    asyncio.run(main())