# Minikube

## Install

Download the latest Minikube

`curl -Lo minikube https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64`

Make it executable

`chmod +x ./minikube`

Move it to your user's executable PATH

`sudo mv ./minikube /usr/local/bin/`

Set the driver version to Docker

`minikube config set driver docker`

## Manage

Start

`minikube start`

Stop

`minikube stop`

Delete all minikube clusters

`minikube delete --all`

## Use with kubectl

```bash
kubectl config use-context minikube

# Start minikube again to enable kubectl in it
minikube start

kubectl get pods -A
```
