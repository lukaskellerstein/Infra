# Deploy

```bash
kubectl apply -f all.yaml
```

# AKS

The k8s nodes needs to support `nested virtualization`.

Ex. `Dv3` and `Dsv3` does.

Dv3
https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/general-purpose/dv3-series?tabs=sizebasic

Dsv3
https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/general-purpose/dsv3-series?tabs=sizebasic

# Access

## Minikube

```bash
minikube service qemu
```
