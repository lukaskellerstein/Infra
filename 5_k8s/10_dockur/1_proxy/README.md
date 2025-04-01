# Deploy

Traefik

```bash
kubectl apply -f traefik.yml
```

Dockur/Windows

```bash
kubectl apply -f all.yaml
```

# Access

## Minikube

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
