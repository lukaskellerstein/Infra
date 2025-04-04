# Deploy App

```bash
kubectl apply -f .
```

# Access

via `http://<NODE_IP>:30080/`

## Minikube

Create a tunnel to the service via `minikube service echo-api`.

Result below. Open then via `http://127.0.0.1:34733`.

```
|-----------|----------|-------------|---------------------------|
| NAMESPACE |   NAME   | TARGET PORT |            URL            |
|-----------|----------|-------------|---------------------------|
| default   | echo-api |          80 | http://192.168.49.2:30080 |
|-----------|----------|-------------|---------------------------|
🏃  Starting tunnel for service echo-api.
|-----------|----------|-------------|------------------------|
| NAMESPACE |   NAME   | TARGET PORT |          URL           |
|-----------|----------|-------------|------------------------|
| default   | echo-api |             | http://127.0.0.1:34733 |
|-----------|----------|-------------|------------------------|
🎉  Opening service default/echo-api in default browser...
👉  http://127.0.0.1:34733
❗  Because you are using a Docker driver on linux, the terminal needs to be open to run it.
```

## AKS

**Not possible**, if nodes don't have public `EXTERNAL-IP`s. -> do load balance
