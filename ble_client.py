import asyncio
# pyrefly: ignore [missing-import]
from bleak import BleakScanner

async def main():
    devices = await BleakScanner.discover()
    for d in devices:
        print(f'{d.name}\n {d.address}\n')
if __name__=="__main__":
    asyncio.run(main()) 