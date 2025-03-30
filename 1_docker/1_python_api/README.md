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
docker build -t my_python_api:0.0.1 .
```

Build without cache

```bash
docker build --no-cache --progress=plain -t my_python_api:0.0.1 .
```

Run

```bash
docker run --name my-python-api -p 8000:8000 my_python_api:0.0.1
```

Tag

```bash
docker tag my_python_api:0.0.1 lukaskellerstein/my_python_api:0.0.1
```

Push

```bash
docker push lukaskellerstein/my_python_api:0.0.1
```

# Test

via curl

```bash
curl http://localhost:8000/
```

```bash
curl http://localhost:8000/status
```

```bash
curl -X POST http://localhost:8000/echo -H "Content-Type: application/json" -d '{"message":"Hello from curl!"}'
```
