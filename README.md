# Electricity Meter Optical Baud Rate Finder

## Description
This script is used to discover the baud rate at which an electricity meter is communicating on via a serial connection to an optical IR transceiver.

## Requirements
- Python
- Pip
- GuruX python library

## Installation
To install the necessary python packages run `pip install -r requirements.txt` from the command line within the project folder. This will download the packages automatically.

## Usage
The script takes two parameters:
- Serial Port - The serial port on which the optical IR transceiver is connected.
- Timeout (optional - default is 5000ms) - The time in milliseconds to wait for a reply from the meter before giving up.

If a meter responds during the process, the valid baud rate will be returned.

## Examples
Optical IR transceiver is connected to COM1. Timeout is default 5000ms.
```
python meter_baud_finder.py COM1
```

Optical IR transceiver is connected to COM4. Timeout is 1000ms.
```
python meter_baud_finder.py COM1 --timeout 1000
```