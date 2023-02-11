import asyncio
import signal
import websockets


USERS = set()


async def addUser(websocket):
    USERS.add(websocket)


async def removeUser(websocket):
    USERS.remove(websocket)


async def handler(websocket):
    await addUser(websocket)

    try:
        while True:
            message = f"received: {await websocket.recv()}, users: {len(USERS)} path: {websocket.path}"
            await asyncio.wait(
                [user.send(message) for user in USERS]
            )
    finally:
        await removeUser(websocket)


async def main():
    loop = asyncio.get_running_loop()
    stop = loop.create_future()
    loop.add_signal_handler(signal.SIGTERM, stop.set_result, None)

    async with websockets.serve(
        handler,
        host="",
        port=8765
    ):
        await stop


if __name__ == "__main__":
    asyncio.run(main())