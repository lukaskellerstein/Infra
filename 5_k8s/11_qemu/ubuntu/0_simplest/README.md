# Description

Basic usage of QEMU.

QEMU in docker contains VNC port, onVNC websockify and onVNC UI.

---

# Deploy

```bash
kubectl apply -f qemu.yaml
```

# Test

```bash
kubectl run debugbox --image=lukaskellerstein/debug-container:0.0.3 --restart=Never --command -- sh -c "sleep infinity"
kubectl exec -it debugbox -- bash
```

## Test "In cluster" - via POD IP (PODs network)

```bash
# VNC test
nc <POD-IP> 5900            <------ WORKS
# ex. nc 10.244.0.134 5900

# HTTP test
curl <POD-IP>:8006          <------ WORKS
# curl 10.244.0.134:8006
```

## Test "In cluster" - via Service

```bash
# VNC test
nc <SERVICE-NAME> 5900      <------ WORKS
# ex. nc qemu1 5900

# HTTP test
curl <SERVICE-NAME>:8006    <------ WORKS
# ex. curl qemu1:8006
```

## Test "Outside cluster" - via LoadBalancer

```bash
# VNC test
nc <EXTERNAL-IP-OF-SERVICE> 5900        <------ WORKS
# ex. nc 52.250.36.58 5900

# HTTP test
curl <EXTERNAL-IP-OF-SERVICE>:8006      <------ WORKS
# ex. curl 52.250.36.58:8006
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
