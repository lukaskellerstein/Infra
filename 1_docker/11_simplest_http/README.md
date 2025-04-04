# Docker

Build

```bash
docker build -t simple-http-server:0.0.1 .
```

**Build for k8s** = architecture Linux-Amd64

```bash
docker buildx build --platform=linux/amd64 -t simple-http-server:0.0.1 .
```

Run

```bash
docker run -it --rm \
  -e PORT=7600 \
  -p 7600:7600 \
  simple-http-server:0.0.1
```

Tag

```bash
docker tag simple-http-server:0.0.1 lukaskellerstein/simple-http-server:0.0.1
```

Push

```bash
docker push lukaskellerstein/simple-http-server:0.0.1
```

# Test

```bash
curl http://127.0.0.1:7600
```
