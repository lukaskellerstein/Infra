# Description

`Debug` container to investigate contents of PVC (Persistent volume claim) in k8s.

# Docker

Build

```bash
docker build -t debug-container-pvc:0.0.1 .
```

**Build for k8s** = architecture Linux-Amd64

```bash
docker buildx build --platform=linux/amd64 -t debug-container-pvc:0.0.1 .
```

Run

```bash
docker run -it debug-container-pvc:0.0.1
```

Tag

```bash
docker tag debug-container-pvc:0.0.1 lukaskellerstein/debug-container-pvc:0.0.1
```

Push

```bash
docker push lukaskellerstein/debug-container-pvc:0.0.1
```
