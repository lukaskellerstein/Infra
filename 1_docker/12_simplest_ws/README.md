# Docker

Build

```bash
docker build -t simple-ws-server:0.0.1 .
```

**Build for k8s** = architecture Linux-Amd64

```bash
docker buildx build --platform=linux/amd64 -t simple-ws-server:0.0.1 .
```

Run

```bash
docker run -it --rm \
  -e PORT=7700 \
  -p 7700:7700 \
  simple-ws-server:0.0.1
```

Tag

```bash
docker tag simple-ws-server:0.0.1 lukaskellerstein/simple-ws-server:0.0.1
```

Push

```bash
docker push lukaskellerstein/simple-ws-server:0.0.1
```

# Test

```bash
npx wscat -c ws://127.0.0.1:7700
```
