# Deploy

Traefik

```bash
cd proxy
kubectl apply -f namespace.yml
kubectl apply -f traefik.yml
```

Car solution

```bash
cd car_solution
kubectl apply -f namespace.yml
kubectl apply -f db.yml
kubectl apply -f api.yml
kubectl apply -f ui.yml
kubectl apply -f app.yml
```

Ecommerce solution

```bash
cd ecommerce_solution
kubectl apply -f namespace.yml
kubectl apply -f db.yml
kubectl apply -f order-service.yml
kubectl apply -f product-service.yml
kubectl apply -f ui.yml
```

# Access

via `http://<EXTERNAL-IP>/echo`
via `http://<EXTERNAL-IP>/cars`
via `http://<EXTERNAL-IP>/ecommerce`

## ACR

```bash
kubectl get svc traefik-web-service
```

Result

```
NAME                  TYPE           CLUSTER-IP    EXTERNAL-IP      PORT(S)        AGE
traefik-web-service   LoadBalancer   10.0.25.187   172.171.140.64   80:30501/TCP   32m
```

Open `http://172.171.140.64/echo`

## Minikube

Run `minikube service traefik-web-service --namespace=traefik`, then you can open the app via Ex. `http://127.0.0.1:45819/echo`

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
