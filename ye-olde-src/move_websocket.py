import asyncio
from websockets.server import serve
from magna_karta_controller import MagnaKartaController

controller = MagnaKartaController(speed=0.5)


async def echo(websocket):
    async for message in websocket:
        if message == "stop":
            controller.stop()
            continue

        (x_str, y_str) = message.split(",")

        x = float(x_str)
        y = float(y_str)

        x -= 1
        y -= 1

        if abs(x) > abs(y):
            if x < 0:
                controller.left()
            else:
                controller.right()
        else:
            if y < 0:
                controller.forward()
            else:
                controller.backward()


async def main():
    async with serve(echo, "0.0.0.0", 8765):
        await asyncio.Future()


asyncio.run(main())
