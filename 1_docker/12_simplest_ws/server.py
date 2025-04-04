import asyncio
import os
import websockets

PORT = int(os.getenv("PORT", 8765))

async def echo(websocket):
    async for message in websocket:
        await websocket.send(message)

async def main():
    async with websockets.serve(echo, "0.0.0.0", PORT):
        print(f"WebSocket Echo Server running on ws://0.0.0.0:{PORT}")
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())
