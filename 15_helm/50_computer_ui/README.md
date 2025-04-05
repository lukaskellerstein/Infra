# TEST

**Minikube**

```bash
minikube service traefik-service
```

**AKS**

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

## Ubuntu

```bash
helm upgrade --install ubuntu-1-release ./ubuntu-computer
```

```bash
helm uninstall ubuntu-1-release
```

## Windows

```bash
helm upgrade --install windows-1-release ./windows-computer
```

```bash
helm uninstall windows-1-release
```

## MacOS

```bash
helm upgrade --install macos-1-release ./macos-computer
```

```bash
helm uninstall macos-1-release
```
