# **Deployment**

A **Deployment** in Kubernetes manages a group of identical Pods. It ensures that the desired number of replicas are always running and automatically replaces any failed or updated Pods. It's great for stateless apps that need scaling and updates.

**Key features:**

- Self-healing (restarts failed Pods)
- Rolling updates
- Easy scaling

---

# **Service**

A **Service** in Kubernetes provides a stable **network endpoint** to access one or more Pods. Since Pods can change IPs or be replaced, a Service ensures you always have a consistent way to reach them.

**Common types:**

- `ClusterIP` – internal access (default)
- `NodePort` – exposes on a port on each node
- `LoadBalancer` – external access via cloud load balancer

**ALL types:**

| Service Type   | Description                                                  | Use Case                                               |
| -------------- | ------------------------------------------------------------ | ------------------------------------------------------ |
| `ClusterIP`    | Default. Exposes the service on a cluster-internal IP only.  | Internal communication between Pods.                   |
| `NodePort`     | Exposes the service on a static port on each Node’s IP.      | Simple external access for testing/dev.                |
| `LoadBalancer` | Creates an external load balancer (cloud provider required). | External access in cloud environments (e.g. AKS).      |
| `ExternalName` | Maps the service to an external DNS name.                    | Redirect service traffic to an external service.       |
| `Headless`     | (`ClusterIP: None`) Doesn’t allocate a cluster IP.           | Needed for stateful sets, DNS-based service discovery. |

---
