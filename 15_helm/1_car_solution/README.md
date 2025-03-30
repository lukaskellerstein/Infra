# Helm

```bash
helm install <release-name> <chart-dir>
```

- release-name — the label Helm uses to manage this install
- chart-dir — the path to the Helm chart directory (e.g., ./car-solution)

The `--namespace` flag tells Helm where to install the chart in Kubernetes.

## View rendered YAML files

```bash
helm template car-solution-release ./ --namespace car
```

## Apply templates

```bash
helm install car-solution-release ./ --namespace car --create-namespace
```

## Subcharts

Traefik is as subchart for main `car-solution` chart
