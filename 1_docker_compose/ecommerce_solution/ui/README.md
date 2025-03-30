# Run

```bash
python server.py
```

# Docker

Build

```bash
docker build -t ecomm-ui:0.0.1 .
```

Build without cache

```bash
docker build --no-cache --progress=plain -t ecomm-ui:0.0.1 .
```

Tag

```bash
docker tag ecomm-ui:0.0.1 lukaskellerstein/ecomm-ui:0.0.1
```

Push

```bash
docker push lukaskellerstein/ecomm-ui:0.0.1
```
