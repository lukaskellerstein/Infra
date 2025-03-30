import pulumi_kubernetes as k8s

app = k8s.yaml.ConfigFile("my-k8s-app",
    file="./k8s/app.yml")


