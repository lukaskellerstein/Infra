# TEST

Minikube proxy

```bash
minikube service traefik-service
```

AKS

Open EXTERNAL-IP via `http://proxy.20.3.4.110.nip.io`

Dashboard: `http://proxy.20.3.4.110.nip.io:8080/`
UI: `http://proxy.20.3.4.110.nip.io/ui`
Add qemu1 `ws://proxy.20.3.4.110.nip.io:7777/qemu1`

# Deployments

## Traefik Proxy

```bash
helm upgrade --install traefik-release ./traefik
```

```bash
helm uninstall traefik-release
```

## UI

```bash
helm upgrade --install ui-release ./ui
```

```bash
helm uninstall ui-release
```

## Qemu1

```bash
helm upgrade --install qemu-1-release ./qemu-computer
```

```bash
helm uninstall qemu-1-release
```
