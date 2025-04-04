# Deploy

From this folder run commands below.

## Traefik Helm

```Bash
helm install proxy-release ./0_traefik --namespace traefik --create-namespace
```

## Car project Helm

```Bash
helm install car-project-release ./1_car_project --namespace car --create-namespace
```

## Ecommerce solution Helm

```Bash
helm install ecommerce-project-release ./2_ecommerce_project --namespace ecommerce --create-namespace
```

# Access

via `http://<EXTERNAL-IP>/echo`
via `http://<EXTERNAL-IP>/cars`
via `http://<EXTERNAL-IP>/ecommerce`

## AKS

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
