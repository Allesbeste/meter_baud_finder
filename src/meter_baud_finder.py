# Electricity Meter Optical Baud Rate Finder
# Copyright (C) 2023 Edrean Ernst

# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or any later version.

# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>.

import argparse
import time
# from gurux_dlms import *
from gurux_serial.GXSerial import GXSerial
from gurux_common import ReceiveParameters
from gurux_common.io import Parity

# List of baud rates to try
baud_rates = [300, 600, 1200, 1800, 2400, 4800, 7200, 9600, 14400, 19200, 38400, 56000, 57600, 115200, 128000]

def find_valid_baud_rate(serial_port, timeout_ms):
    # client = GXDLMSClient(useLogicalNameReferencing=False, interfaceType=InterfaceType.HDLC_WITH_MODE_E)
    media = GXSerial(port=serial_port, dataBits=7, parity=Parity.EVEN)
    p = ReceiveParameters()
    p.allData = True
    p.eop = '\n'
    p.waitTime = timeout_ms
    media.open()

    for baud_rate in baud_rates:
        print(f"Trying baud rate: {baud_rate}")
        media.baudRate = baud_rate

        # media.open()
        reply_received = False
        with media.getSynchronous():
            data = "/?!\r\n"
            media.send(data)
            if media.receive(p):
                reply_received = True

        # media.close()

        if reply_received:
            print(f"Valid baud rate found: {baud_rate}")
            print(f"Received: {str(p.reply)}")
            media.close()
            return baud_rate

        # Wait for a short time before trying the next baud rate
        time.sleep(1)

    print("No valid baud rate found.")
    media.close()
    return None

def main():
    # Create an ArgumentParser
    parser = argparse.ArgumentParser(description='Find the valid baud rate for communication with an electricity meter.')

    # Add command-line arguments
    parser.add_argument('serial_port', help='The serial port to use for communication (e.g., COM1)')
    parser.add_argument('--timeout', type=int, default=5000, help='The communication timeout in milliseconds')

    # Parse the command-line arguments
    args = parser.parse_args()

    valid_baud_rate = find_valid_baud_rate(args.serial_port, args.timeout)

    if valid_baud_rate is not None:
        print(f"Use this baud rate for communication: {valid_baud_rate}")

if __name__ == "__main__":
    main()
