import asyncio
import os
import websockets
from datetime import datetime
import traceback

LISTEN_HOST = os.environ.get("LISTEN_HOST", "0.0.0.0")
LISTEN_PORT = int(os.environ.get("LISTEN_PORT", "7500"))
VNC_TARGET_HOST = os.environ.get("VNC_HOST", "host.docker.internal")
VNC_TARGET_PORT = int(os.environ.get("VNC_PORT", "5900"))

print(f"LISTEN_HOST: {LISTEN_HOST}")
print(f"LISTEN_PORT: {LISTEN_PORT}")
print(f"VNC_TARGET_HOST: {VNC_TARGET_HOST}")
print(f"VNC_TARGET_PORT: {VNC_TARGET_PORT}")

def log(msg):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{now}] {msg}", flush=True)

async def proxy_handler(websocket):
    client_ip = websocket.remote_address[0]
    log(f"🔌 New WebSocket connection from {client_ip}")

    try:
        reader, writer = await asyncio.open_connection(VNC_TARGET_HOST, VNC_TARGET_PORT)
        log(f"➡️  Connected to VNC server at {VNC_TARGET_HOST}:{VNC_TARGET_PORT}")

        async def ws_to_tcp():
            async for message in websocket:
                writer.write(message)
                await writer.drain()
                log(f"⏩ WebSocket → VNC: {len(message)} bytes")

        async def tcp_to_ws():
            while True:
                data = await reader.read(1024)
                if not data:
                    log(f"⛔ VNC server closed the connection")
                    break
                await websocket.send(data)
                log(f"⏪ VNC → WebSocket: {len(data)} bytes")

        await asyncio.gather(ws_to_tcp(), tcp_to_ws())

    except Exception as e:
        log(f"❗ Error: {e}")
        traceback.print_exc()
    finally:
        try:
            writer.close()
            await writer.wait_closed()
        except:
            pass
        log(f"🔌 Closed connection with {client_ip}")

async def main():
    log(f"🚀 Starting proxy: ws://{LISTEN_HOST}:{LISTEN_PORT} → {VNC_TARGET_HOST}:{VNC_TARGET_PORT}")
    async with websockets.serve(proxy_handler, LISTEN_HOST, LISTEN_PORT, max_size=None, ping_interval=None):
        await asyncio.Future()

if __name__ == '__main__':
    asyncio.run(main())
