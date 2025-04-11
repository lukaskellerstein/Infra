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
docker build -t python-script-azure-1:0.0.1 .
```

Build without cache

```bash
docker build --no-cache --progress=plain -t python-script-azure-1:0.0.1 .
```

**Build for k8s** = architecture Linux-Amd64

```bash
docker buildx build --platform=linux/amd64 -t python-script-azure-1:0.0.1 .
```

Run

```bash
docker run --name my-python-script-azure-1 python-script-azure-1:0.0.1
```

Tag

```bash
docker tag python-script-azure-1:0.0.1 lukaskellerstein/python-script-azure-1:0.0.1
```

Push

```bash
docker push lukaskellerstein/python-script-azure-1:0.0.1
```
