# Service

| Service Type   | Description                                                  | Use Case                                               |
| -------------- | ------------------------------------------------------------ | ------------------------------------------------------ |
| `ClusterIP`    | Default. Exposes the service on a cluster-internal IP only.  | Internal communication between Pods.                   |
| `NodePort`     | Exposes the service on a static port on each Node’s IP.      | Simple external access for testing/dev.                |
| `LoadBalancer` | Creates an external load balancer (cloud provider required). | External access in cloud environments (e.g. AKS).      |
| `ExternalName` | Maps the service to an external DNS name.                    | Redirect service traffic to an external service.       |
| `Headless`     | (`ClusterIP: None`) Doesn’t allocate a cluster IP.           | Needed for stateful sets, DNS-based service discovery. |

### ✅ 1. **NodePort (Easy for Dev/Test)**

- Exposes the service on a static port on each Node's IP.
- Accessible via `http://<node-ip>:<nodePort>`

**How to use it:**

```yaml
apiVersion: v1
kind: Service
metadata:
  name: my-service
spec:
  type: NodePort
  selector:
    app: my-app
  ports:
    - port: 80 # Service port
      targetPort: 8080 # Pod port
      nodePort: 30080 # External port (in the range 30000-32767)
```

➡️ **Pros**: Easy to set up  
➡️ **Cons**: Not secure or scalable, port range is limited

---

### ✅ 2. **LoadBalancer (Best for Cloud Providers)**

- Automatically provisions an external IP using a cloud provider’s load balancer (AWS, Azure, GCP).

**How to use it:**

```yaml
apiVersion: v1
kind: Service
metadata:
  name: my-service
spec:
  type: LoadBalancer
  selector:
    app: my-app
  ports:
    - protocol: TCP
      port: 80
      targetPort: 8080
```

➡️ **Pros**: Simple, automatic IP allocation  
➡️ **Cons**: Only works on cloud (not in bare-metal or Minikube without addons)

---

### ✅ 3. **Ingress (Best for Multiple Services + Domain Support)**

- Uses an Ingress Controller (like **Traefik**, **NGINX**) and routes traffic via hostname/path.

**Basic example:**

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: my-ingress
spec:
  rules:
    - host: my-app.example.com
      http:
        paths:
          - path: /
            pathType: Prefix
            backend:
              service:
                name: my-service
                port:
                  number: 80
```

➡️ **Pros**: Clean, supports TLS, domain routing, path-based routing  
➡️ **Cons**: Requires Ingress controller setup

---

### ✅ 4. **Port Forwarding (Quick Dev Access)**

For temporary access to a pod/service:

```bash
kubectl port-forward service/my-service 8080:80
```

➡️ Access via `localhost:8080`

➡️ **Pros**: Zero setup  
➡️ **Cons**: Only for development/debugging

---

### ✅ Summary: Which one should I use?

| Method       | Best For                         | External IP? | TLS/Domain? | Easy Setup |
| ------------ | -------------------------------- | ------------ | ----------- | ---------- |
| NodePort     | Local dev or testing             | ✅ (manual)  | ❌          | ✅✅✅     |
| LoadBalancer | Cloud deployments                | ✅ (auto)    | ❌          | ✅✅✅     |
| Ingress      | Real-world apps, multiple routes | ✅ (via LB)  | ✅          | ✅✅       |
| Port Forward | Local testing/dev                | ❌           | ❌          | ✅✅✅✅   |
