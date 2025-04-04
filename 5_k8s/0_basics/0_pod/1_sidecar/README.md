# Description

Sidecar implementation => Running two containers in one pod.

# Deploy

```bash
kubectl apply -f app.yaml
```

# Test

We can make the test "inside the cluster" via debugbox container.
We can make the test "outside the cluster" via loadbalancer or proxy.

## Test "In cluster" - via POD IP (PODs network)

From debugbox

```bash
kubectl run debugbox --image=lukaskellerstein/debug-container:0.0.3 --restart=Never --command -- sh -c "sleep infinity"
kubectl exec -it debugbox -- bash
```

```bash
# HTTP test
curl <POD-IP>:8080
# ex. curl 10.244.0.134:8080

# Websocket test
npx wscat -c http://<POD-IP>:7070
# ex. npx wscat -c http://10.244.0.134:7070
```

## Test "In cluster" - via Service

- We are not using `service`

## Test "Outside cluster" - via LoadBalancer

- We are not using `service` with type `LoadBalancer`

## Test "Outside cluster" - via Traefik

- We are not using `service`
- We are not using `traefik` proxy
