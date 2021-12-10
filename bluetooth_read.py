
"""
Reads and prints scale data
--------------------------------------------------
Reads and prints out data from bluetooth (BLE) of an A&D SJ-6000WP-BT digital weight scale.
Requires bleak: pip install bleak

Created on 2021-12-10 by Johannes Nicholas (goanna7007) <goanna7007@gmail.com>
"""

import asyncio
from bleak import BleakClient

async def run_ble_client(address: str, char_uuid: str):
    async def callback_handler(sender, data):
        print(data.decode(), end = "")

    async with BleakClient(address) as client:
        print(f"Connected: {client.is_connected}")
        await client.start_notify(char_uuid, callback_handler)
        # wait forever
        await asyncio.Event().wait()


if __name__ == "__main__":
    asyncio.run(
        run_ble_client("fb:f3:ea:5c:61:61","5699d646-0c53-11e7-93ae-92361f002671",)
    )
