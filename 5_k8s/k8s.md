### 1. **Deployment**

**Purpose:** Manages stateless applications. Ensures desired number of pods are running.

- Handles updates, rollbacks, replicas.
- Typically used for web servers, APIs, etc.

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-app
spec:
  replicas: 3
  selector:
    matchLabels:
      app: my-app
  template:
    metadata:
      labels:
        app: my-app
    spec:
      containers:
        - name: app-container
          image: my-app:latest
```

---

### 2. **Service**

**Purpose:** Exposes your application (pods) to the network inside or outside the cluster.

- **ClusterIP** (default): Internal access only.
- **NodePort**: Accessible via port on each Node.
- **LoadBalancer**: Creates external IP via cloud provider.

```yaml
apiVersion: v1
kind: Service
metadata:
  name: my-app-service
spec:
  selector:
    app: my-app
  ports:
    - port: 80
      targetPort: 8080
  type: ClusterIP
```

---

### 3. **ConfigMap**

**Purpose:** Inject configuration data (non-sensitive) into pods.

- Mounted as env vars or files.
- Keeps config separate from code.

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
data:
  APP_MODE: "production"
  LOG_LEVEL: "info"
```

---

### 4. **Secret**

**Purpose:** Similar to ConfigMap but for **sensitive data** like passwords or tokens.

- Base64-encoded values.
- Mounted as env vars or files.

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: app-secret
type: Opaque
data:
  DB_PASSWORD: cGFzc3dvcmQ= # "password" base64
```

---

### 5. **PersistentVolume (PV)**

**Purpose:** Represents actual physical storage in the cluster.

- Created manually or dynamically (via a StorageClass).

```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: my-pv
spec:
  capacity:
    storage: 1Gi
  accessModes:
    - ReadWriteOnce
  hostPath:
    path: /data/myapp
```

---

### 6. **PersistentVolumeClaim (PVC)**

**Purpose:** A request for storage by a pod. Binds to a PV.

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: my-pvc
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 500Mi
```

---

### 7. **StatefulSet**

**Purpose:** Manages **stateful applications** (like databases).

- Stable network identity (DNS), storage, and ordering.

```yaml
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: mysql
spec:
  serviceName: "mysql"
  replicas: 1
  selector:
    matchLabels:
      app: mysql
  template:
    metadata:
      labels:
        app: mysql
    spec:
      containers:
        - name: mysql
          image: mysql:5.7
```

---

### 8. **Ingress**

**Purpose:** Manages external access (HTTP/HTTPS) to services.

- Works with an Ingress Controller (like NGINX, Traefik).

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: app-ingress
spec:
  rules:
    - host: myapp.example.com
      http:
        paths:
          - path: /
            pathType: Prefix
            backend:
              service:
                name: my-app-service
                port:
                  number: 80
```

---

### 9. **Job / CronJob**

**Purpose:**

- **Job:** One-time task (e.g. DB migration).
- **CronJob:** Scheduled tasks (like `cron`).

```yaml
# CronJob example
apiVersion: batch/v1
kind: CronJob
metadata:
  name: cleanup-job
spec:
  schedule: "0 3 * * *"
  jobTemplate:
    spec:
      template:
        spec:
          containers:
            - name: cleaner
              image: cleanup:latest
          restartPolicy: OnFailure
```

---

Want me to generate a full working example with `Deployment`, `Service`, `ConfigMap`, and `PVC` all working together?
