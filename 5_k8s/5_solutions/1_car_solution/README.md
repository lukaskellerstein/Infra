# Deploy

## Car solution

Using `car` namespace for the "car solution".
Using `traefik` namespace for the proxy.

1. We need to create the proxy

`kubectl apply -f traefik.yml`

2. The rest for car solution

```bash
kubectl apply -f namespace.yml
kubectl apply -f db.yml
kubectl apply -f api.yml
kubectl apply -f ui.yml
kubectl apply -f app.yml
```

# Access

via `http://<EXTERNAL-IP>`

## ACR

```bash
kubectl get svc traefik-web-service
```

Result

```
NAME                  TYPE           CLUSTER-IP    EXTERNAL-IP      PORT(S)        AGE
traefik-web-service   LoadBalancer   10.0.25.187   172.171.140.64   80:30501/TCP   32m
```

Open `http://172.171.140.64/cars`

## Minikube

Run `minikube service traefik-web-service`, then you can open the app via Ex. `http://127.0.0.1:45819/cars`

**REASON:**

Minikube does not support **load balancer** directly.

So you will see for command

```bash
kubectl get svc traefik-web-service
```

**Pending** external IP

```
NAME                  TYPE           CLUSTER-IP     EXTERNAL-IP   PORT(S)        AGE
traefik-web-service   LoadBalancer   10.99.175.29   <pending>     80:30704/TCP   35s
```
