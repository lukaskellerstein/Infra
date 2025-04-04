# Deploy

```bash
kubectl apply -f all.yaml
```

# Test

Connect to the debug container

```bash
kubectl run debugbox --image=lukaskellerstein/debug-container:0.0.3 --restart=Never --command -- sh -c "sleep infinity"
kubectl exec -it debugbox -- bash
```

Test the servers

```bash
# HTTP test
curl <POD-IP>:8080

# Websocket test
npx wscat -c ws://<POD-IP>:7070
```
