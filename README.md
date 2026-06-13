# 📡 OpenBandLab

OpenBandLab is an asynchronous Bluetooth Low Energy (BLE) reverse-engineering and telemetry capture suite built on Python and the [Bleak](https://github.com/hbldh/bleak) library. It provides utilities for discovering, probing, and logging custom GATT services and notification channels from target BLE devices (e.g., smart bands, fitness trackers, or sensor peripherals).

The project is structured around a specific target BLE peripheral with MAC address `44:27:F3:21:47:BC`.

---

## 🚀 Key Features

- **Automated Service Discovery**: Recursively enumerates services, characteristics, and descriptors.
- **Dynamic Probing**: Scans characteristics and automatically subscribes to all available notification/indication channels.
- **Multi-Channel Logging**: Concurrently listens to up to 9 separate data notification channels and logs packets to disk.
- **Command Injection Testing**: Utility to write custom payloads (e.g., GATT writes) to investigate device state responses.
- **Structured Telemetry Capture**: Saves time-stamped hex packets for post-processing and analysis.

---

## 📂 Repository Index

| File / Directory | Description |
| :--- | :--- |
| **`notificn.py`** | Main session capture script. Subscribes to 9 concurrent notification channels (`51` through `59`) and logs packets with millisecond timestamps to the `captures/` folder. |
| **`all_readables.py`** | Scans and attempts to read every readable characteristic across all services, outputting data length, Hex representation, and UTF-8 decoded text where applicable. |
| **`probe.py`** | Automated notify prober. Discovers all characteristics supporting notifications and attempts to subscribe to them. |
| **`ble_client.py`** | Targeted notification listener specifically configured for characteristic `51`. |
| **`tooltest.py`** | Command write tester. Probes write capability by sending a control command (`0x00`) to characteristic `52`. |
| **`descriptors.py`** | Reserved workspace module for characteristic descriptors and parsing utilities. |
| **`research.md`** | Dedicated research notes and reverse-engineering findings log. |
| **`captures/`** | Directory where raw telemetry log files (format: `session_YYYYMMDD_HHMMSS.log`) are saved. |

---

## 🎛️ GATT Characteristic Reference

Based on protocol reverse-engineering, the target BLE device uses the standard Bluetooth base UUID prefix (`0000xxxx-0000-1000-8000-00805f9b34fb`) with the following map:

| Short ID | Characteristic UUID | Properties | Purpose |
| :---: | :--- | :--- | :--- |
| **`50`** | `00000050-0000-1000-8000-00805f9b34fb` | `Read` | **Bootstrap/Initialization**: Retreived once during startup sequence to verify handshake. |
| **`51`** | `00000051-0000-1000-8000-00805f9b34fb` | `Notify` | **Primary Telemetry**: Continuous sensor/status telemetry notifications. |
| **`52`** | `00000052-0000-1000-8000-00805f9b34fb` | `Write`, `Notify` | **Control/Feedback**: Used for command writes and associated feedback notifications. |
| **`53` – `59`** | `0000005[3-9]-0000-1000-8000-00805f9b34fb` | `Notify` | **Extended Data Channels**: Multi-channel streaming telemetry. |

---

## 🛠️ Setup & Installation

### 1. Prerequisites
- **Python 3.10+**
- BLE-compatible hardware (Bluetooth 4.0+ adapter)
- OS-level BLE permissions (especially on Linux/macOS; Windows standard permissions are usually sufficient)

### 2. Install Dependencies
Create a virtual environment and install the required library:
```bash
# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows, use: .venv\Scripts\activate

# Install Bleak
pip install bleak
```

### 3. Configure MAC Address
If you are interacting with a different device, update the `ADDRESS` variable in the scripts:
```python
ADDRESS = "YOUR_DEVICE_MAC_ADDRESS"
```

---

## 📈 Usage Guide

### Capturing Telemetry Data
Run `notificn.py` to initiate a capture session. It will connect to the device, subscribe to all channels, and write the telemetry data in real-time:
```bash
python notificn.py
```
This logs data into the `captures/` folder using the following format:
```
[18:03:53.015] UUID=00000051-0000-1000-8000-00805f9b34fb LEN=21 HEX=00000201714ac32021f9363444b9b73a42caf99ebf
```

### Exploring Readable Values
To view values of all readable characteristics:
```bash
python all_readables.py
```

### Scanning Notifications
To dynamically subscribe to all notify-supporting services:
```bash
python probe.py
```

---

## 🧪 Testing Commands
To send a raw write command (e.g. bootstrap response test) to Characteristic `52`:
```bash
python tooltest.py
```

---

## 📝 License & Contributions
This project is for research and reverse-engineering purposes. Pull requests to expand the parser in `descriptors.py` or findings in `research.md` are welcome.

