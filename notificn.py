import asyncio
from datetime import datetime
from pathlib import Path

from bleak import BleakClient

ADDRESS = "44:27:F3:21:47:BC"

CHANNELS = [
    "00000051-0000-1000-8000-00805f9b34fb",
    "00000052-0000-1000-8000-00805f9b34fb",
    "00000053-0000-1000-8000-00805f9b34fb",
    "00000054-0000-1000-8000-00805f9b34fb",
    "00000055-0000-1000-8000-00805f9b34fb",
    "00000056-0000-1000-8000-00805f9b34fb",
    "00000057-0000-1000-8000-00805f9b34fb",
    "00000058-0000-1000-8000-00805f9b34fb",
    "00000059-0000-1000-8000-00805f9b34fb",
]

LOG_DIR = Path("captures")
LOG_DIR.mkdir(exist_ok=True)

LOG_FILE = LOG_DIR / (
    f"session_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
)


def log(msg: str):
    print(msg)

    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(msg + "\n")


def create_handler(uuid: str):
    def handler(sender, data):
        ts = datetime.now().strftime("%H:%M:%S.%f")[:-3]

        packet = (
            f"[{ts}] "
            f"UUID={uuid} "
            f"LEN={len(data)} "
            f"HEX={data.hex()}"
        )

        log(packet)

    return handler


async def main():
    log("=" * 80)
    log("OPENBANDLAB BLE CAPTURE SESSION")
    log("=" * 80)
    log(f"DEVICE : {ADDRESS}")
    log(f"LOGFILE: {LOG_FILE}")
    log("")

    async with BleakClient(ADDRESS) as client:

        log("CONNECTED")
        log("")

        for uuid in CHANNELS:
            try:
                await client.start_notify(
                    uuid,
                    create_handler(uuid)
                )

                log(f"[OK] SUBSCRIBED {uuid}")

            except Exception as e:
                log(f"[FAIL] {uuid} -> {e}")

        log("")
        log("CAPTURING...")
        log("Press Ctrl+C to stop.")
        log("")

        while True:
            await asyncio.sleep(1)


if __name__ == "__main__":
    try:
        asyncio.run(main())

    except KeyboardInterrupt:
        print("\nCapture stopped.")