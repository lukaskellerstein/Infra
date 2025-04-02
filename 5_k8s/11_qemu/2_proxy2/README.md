# Deploy

Traefik

```bash
kubectl apply -f traefik.yml
```

Qemu1

```bash
kubectl apply -f qemu1.yaml
```

Qemu2

```bash
kubectl apply -f qemu2.yaml
```

Guacamole

```bash
kubectl apply -f guacamole.yaml
```

# Access

## Minikube 1

```bash
minikube service traefik-web-service --namespace traefik
minikube service traefik-dashboard-service --namespace traefik
```

## Minikube 2

1. Change /etc/hosts (on Windows !! not in wsl2)

```bash
notepad C:\Windows\System32\drivers\etc\hosts
```

add line

```
127.0.0.1 windows.example.com
```

2. Do a port forward from k8s

```bash
kubectl port-forward svc/traefik-web-service 8080:80 -n traefik
```

3. Open

```
http://windows.example.com:8080/
```

## ACR
