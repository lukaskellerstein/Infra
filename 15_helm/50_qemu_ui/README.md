# TEST

## Test from outside of the cluster (via Traefik proxy)

Minikube proxy

```bash
minikube service traefik-service
```

```bash
# VNC test
nc <TRAEFIK-WEB-SERVICE-IP> <TRAEFIK-WEB-SERVICE-PORT>      <---- ???
# Websocket test
npx wscat -c ws://<TRAEFIK-WEB-SERVICE-URL>/my-ws           <---- ???
# HTTP test
curl http://<TRAEFIK-WEB-SERVICE-URL>/my-http               <---- WORKS
```

## Test from inside of the cluster (outside a pod)

Connect to the `Debug container`

```bash
kubectl exec -it debugbox -- bash
```

```bash
# Websocket test
npx wscat -c ws://<VNC-WS-PROXY-POD-IP>:7500    <---- WORKS

# HTTP test
curl http://<HTTP-SERVER-POD-IP>:7600           <---- WORKS

# VNC test
nc <QEMU-POD-IP> 5900                           <---- WORKS
```

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

## VNC-WS Proxy

```bash
helm upgrade --install custom-proxy-release ./vnc-ws-proxy
```

```bash
helm uninstall custom-proxy-release
```

## Qemu1

```bash
helm upgrade --install qemu-1-release ./qemu-computer
```

```bash
helm uninstall qemu-1-release
```
