# Run

```bash
uv run main.py
```

or

```bash
uv run -m main
```

# Docker

Build

```bash
docker build -t car-app:0.0.1 .
```

Build without cache

```bash
docker build --no-cache --progress=plain -t car-app:0.0.1 .
```

Run

```bash
docker run --name car-app car-app:0.0.1
```

Tag

```bash
docker tag car-app:0.0.1 lukaskellerstein/car-app:0.0.1
```

Push

```bash
docker push lukaskellerstein/car-app:0.0.1
```
