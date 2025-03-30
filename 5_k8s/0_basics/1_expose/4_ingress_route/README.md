# Notes

> USE CUSTOM `traefik` namespace !!!!
> USE `INGRESS ROUTE` crd

# Deploy

## Traefik

First we need to deploy traefik and set it as k8s ingress controller.

```bash
kubectl apply -f traefik.yml
```

## App

Deploy app

```bash
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

Open `http://172.171.140.64/echo`

## Minikube

Run `minikube service traefik-web-service`, then you can open the app via Ex. `http://127.0.0.1:45819/echo`

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
