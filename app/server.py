import os
import asyncio
import json
import logging
import websockets

from fibtools import fibonacci


async def handler(websocket):
    """
    Handles event construction and response logic
    :param websocket: the target websocket
    """
    dir_path = os.path.dirname(__file__)
    fpath = os.path.join(dir_path, 'fibtools/precomputed_numbers.json')
    fib_helper = fibonacci.FibonacciHelper(fpath)

    async for message in websocket:

        event = json.loads(message)

        # sending ack event
        ack_event = {
            "event_type": "ack",
            "header": "Request Acknowledged: ",
            "message": "event received",
        }

        await websocket.send(json.dumps(ack_event))

        try:
            start, end = int(event["start"]), int(event["end"])
            fib_out = fib_helper.get_fib_seq(start, end)

            # send success event
            success_event = {
                "event_type": "success",
                "header": "Sequence: ",
                "message": str(fib_out),
            }

            await websocket.send(json.dumps(success_event))
            logging.info(success_event["event_type"])

        except Exception as e:
            # sending error event
            error_event = {
                "event_type": "error",
                "header": "Error: ",
                "message": str(e),
            }

            await websocket.send(json.dumps(error_event))
            logging.warning(error_event["event_type"] + error_event["message"])


async def main():
    async with websockets.serve(
            handler, "localhost", 8765, ping_interval=None):
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())
