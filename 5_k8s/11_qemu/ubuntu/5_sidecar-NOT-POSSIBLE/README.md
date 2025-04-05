# Description

Basic usage of QEMU.

QEMU in docker contains VNC port, onVNC websockify and onVNC UI.

We added our custom sidecars - HTTP server + WS server

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

> Sidecar servers DOES NOT WORK with QEMU !!!!!!!!!
>
> QEMU holds all traffic

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# Deploy

```bash
kubectl apply -f qemu.yaml
```

# Test

Connect to the debug container

```bash
kubectl run debugbox --image=lukaskellerstein/debug-container:0.0.3 --restart=Never --command -- sh -c "sleep infinity"
kubectl exec -it debugbox -- bash
```

## Test "In cluster" - via POD IP (PODs network)

```bash
# VNC test
nc <POD-IP> 5900                            <------ WORKS
# ex. nc 10.244.0.134 5900

# noVNC UI - HTTP test
curl <POD-IP>:8006                          <------ WORKS
# ex. curl 10.244.0.134:8006

# Websocket test
npx wscat -c http://<POD-IP>:7070           <------ DOES NOT WORKS
# ex. npx wscat -c http://10.244.0.134:7070

# HTTP test
curl <POD-IP>:8080                          <------ DOES NOT WORKS
# ex. curl 10.244.0.134:8080
```

## Test "In cluster" - via Service

```bash
# VNC test
nc <SERVICE-NAME> 5900                      <------ WORKS
# ex. nc qemu1 5900

# noVNC UI - HTTP test
curl <SERVICE-NAME>:8006                    <------ DOES NOT WORKS
# ex. curl qemu1:8006

# Websocket test
npx wscat -c http://<SERVICE-NAME>:8002     <------ DOES NOT WORKS
# ex. npx wscat -c http://qemu1:8002

# HTTP test
curl <SERVICE-NAME>:8001                    <------ DOES NOT WORKS
# ex. curl qemu1:8001
```

## Test "Outside cluster" - via LoadBalancer

```bash
# VNC test
nc <EXTERNAL-IP-OF-SERVICE> 5900                    <------ WORKS
# ex. nc 52.250.36.58 5900

# noVNC UI - HTTP test
curl <EXTERNAL-IP-OF-SERVICE>:8006                  <------ DOES NOT WORKS
# ex. curl 52.250.36.58:8006

# Websocket test
npx wscat -c http://<EXTERNAL-IP-OF-SERVICE>:8002   <------ DOES NOT WORKS
# ex. npx wscat -c http://52.250.36.58:8002

# HTTP test
curl <EXTERNAL-IP-OF-SERVICE>:8001                  <------ DOES NOT WORKS
# ex. curl 52.250.36.58:8001
```

### AKS

`LoadBalancer` service has working EXTERNAL-IP, use it.

### Minikube

Expose the `LoadBalancer` service

```bash
minikube service qemu
```

## Test "Outside cluster" - via Traefik

- Not possible, because we are not using traefik proxy
