# Pod

A **Pod** is the smallest deployable unit in Kubernetes. It represents **one or more containers** that:

- **Run on the same node**
- **Share the same network IP and storage**
- Are managed as a single unit

In most cases, a Pod contains just **one container**, but it can have multiple if needed — e.g., for tightly coupled helper processes (sidecars).

Think of a Pod as a **wrapper around your container(s)** that Kubernetes uses to manage and schedule them.
