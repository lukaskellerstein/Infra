```bash
kubectl apply -f debug.yaml
kubectl exec -it pvc-inspector -- bash
ls -lah /mnt/pvc
```
