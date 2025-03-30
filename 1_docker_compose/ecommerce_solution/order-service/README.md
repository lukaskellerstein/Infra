# Run

```bash
python server.py
```

# Docker

Build

```bash
docker build -t ecomm-order-svc:0.0.1 .
```

Build without cache

```bash
docker build --no-cache --progress=plain -t ecomm-order-svc:0.0.1 .
```

Tag

```bash
docker tag ecomm-order-svc:0.0.1 lukaskellerstein/ecomm-order-svc:0.0.1
```

Push

```bash
docker push lukaskellerstein/ecomm-order-svc:0.0.1
```
