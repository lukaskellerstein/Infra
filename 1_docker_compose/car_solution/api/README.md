# Run

```bash
uv run server.py
```

or

```bash
uv run -m server
```

# Docker

Build

```bash
docker build -t car-api:0.0.1 .
```

Build without cache

```bash
docker build --no-cache --progress=plain -t car-api:0.0.1 .
```

Run

```bash
docker run --name car-api -p 8000:8000 car-api:0.0.1
```

Tag

```bash
docker tag car-api:0.0.1 lukaskellerstein/car-api:0.0.1
```

Push

```bash
docker push lukaskellerstein/car-api:0.0.1
```

# Test

via curl

```bash
curl http://localhost:8000/healthcheck
```
