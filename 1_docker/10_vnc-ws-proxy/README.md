# Run

```bash
uv run server.py
```

# Docker

Build

```bash
docker build -t vnc-ws-proxy:0.0.1 .
```

**Build for k8s** = architecture Linux-Amd64

```bash
docker buildx build --platform=linux/amd64 -t vnc-ws-proxy:0.0.1 .
```

Run

```bash
docker run -it --rm \
  -e VNC_HOST=host.docker.internal \
  -e VNC_PORT=63795 \
  -e LISTEN_PORT=7500 \
  -p 7500:7500 \
  vnc-ws-proxy:0.0.1
```

Tag

```bash
docker tag vnc-ws-proxy:0.0.1 lukaskellerstein/vnc-ws-proxy:0.0.1
```

Push

```bash
docker push lukaskellerstein/vnc-ws-proxy:0.0.1
```

# Test

```bash
wscat -c ws://127.0.0.1:7500
```
