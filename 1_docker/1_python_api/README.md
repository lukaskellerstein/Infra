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
docker build -t my_python_api_1 .
```

Build without cache

```bash
docker build --no-cache --progress=plain -t my_python_api_1 .
```

Run

```bash
docker run --name my-python-api-1 -p 8000:8000 my_python_api_1:latest
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
