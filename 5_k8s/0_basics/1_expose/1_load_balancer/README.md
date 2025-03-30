# Deploy

## App

```bash
kubectl apply -f .
```

# Access

via `http://<EXTERNAL-IP>`

## AKS

```bash
kubectl get svc echo-api
```

Result

```
NAME       TYPE           CLUSTER-IP   EXTERNAL-IP     PORT(S)        AGE
echo-api   LoadBalancer   10.0.92.26   57.152.50.124   80:31220/TCP   38s
```

Open via `http://57.152.50.124`

## Minikube

Minikube does not support **load balancer** directly.

So you will see for command

```bash
kubectl get svc echo-api
```

**Pending** external IP

```
NAME       TYPE           CLUSTER-IP     EXTERNAL-IP   PORT(S)        AGE
echo-api   LoadBalancer   10.99.175.29   <pending>     80:30704/TCP   35s
```

### Option via Tunnel

```bash
minikube tunnel
```

Result

```
✅  Tunnel successfully started

📌  NOTE: Please do not close this terminal as this process must stay alive for the tunnel to be accessible ...

❗  The service/ingress echo-api requires privileged ports to be exposed: [80]
🔑  sudo permission will be asked for it.
🏃  Starting tunnel for service echo-api.
❗  The service/ingress traefik-ingress requires privileged ports to be exposed: [80 443]
🔑  sudo permission will be asked for it.
🏃  Starting tunnel for service traefik-ingress.
```

Open via `http://localhost:80`
