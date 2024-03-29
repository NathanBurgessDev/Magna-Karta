import asyncio
from websockets.server import serve
from magna_karta_controller import MagnaKartaController

controller = MagnaKartaController(speed=0.5)


async def echo(websocket):
    async for message in websocket:
        (x_str, y_str) = message.split(",")

        x = float(x_str)
        y = float(y_str)
        

        if y > 0.5:
            controller.forward()
        else:
            controller.backward()


async def main():
    async with serve(echo, "localhost", 8765):
        await asyncio.Future()


asyncio.run(main())
