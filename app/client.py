import asyncio
import websockets
import json


async def main():
    """
    Initializes websocket connection
    """
    uri = "ws://localhost:8765"
    async with websockets.connect(uri, ping_interval=None) as websocket:
        await handler(websocket)


async def handler(websocket):
    """
    Handles producer-consumer event logic
    :param websocket: the websocket we're connecting to
    """
    while True:
        message = await producer()
        await websocket.send(message)
        response = await websocket.recv()
        await consumer(response)
        response = await websocket.recv()
        await consumer(response)


async def producer():
    """
    Handles event construction and sends to backend
    :return: serialized input event
    """
    start = input("Enter starting index: ")
    end = input("Enter ending index: ")
    input_event = {
        "event_type": "input",
        "start": start,
        "end": end,
    }
    return json.dumps(input_event)


async def consumer(event):
    """
    Consumes event data and prints to console
    :param event: the event
    """
    event = json.loads(event)
    print(event["header"] + event["message"])


if __name__ == "__main__":
    asyncio.run(main())
