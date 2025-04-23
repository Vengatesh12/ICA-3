
This project demonstrates how to deploy a **WordPress stack** with a **Nginx reverse proxy** using **Helm charts** and **GitOps** practices via **Argo CD**. The entire setup is deployed on a Kubernetes cluster with each component isolated into separate namespaces for better resource management and security.

---

## 🚀 Project Overview

### Objectives:
- Deploy a containerized WordPress application stack.
- Set up Nginx as a reverse proxy for external traffic.
- Create and manage Helm charts for each component (Nginx, WordPress, and MariaDB).
- Use GitOps with **Argo CD** to automatically deploy Kubernetes resources from this repository.

---

## 🧰 Tech Stack

- **Kubernetes**
- **Helm**
- **Argo CD**
- **GitHub**
- **WordPress** (`wordpress:latest`)
- **MariaDB** (`mariadb:10.6.4-focal`)
- **Nginx**
- **SealedSecrets/SOPS** (for sensitive data encryption)

---

## 📁 Repository Structure

```
wordpress-gitops-k8s/
├── nginx-proxy/
│   └── helm-chart/
├── wordpress/
│   └── helm-chart/
├── database/
│   └── helm-chart/
├── manifests/           # Optional base manifests
├── argocd/              # App configurations for Argo CD
├── secrets/             # Encrypted secrets
└── README.md
```

---

## 🧪 Features

- ✅ GitOps deployment with **Argo CD**
- ✅ Isolated **namespaces** for `nginx`, `wp`, and `db`
- ✅ Custom **Helm charts** for all services
- ✅ External access only via **Nginx reverse proxy**
- ✅ Secure handling of **Secrets**
- ✅ Kubernetes resource **labeling** (as per policy)

---

## 📦 Deployment Steps

### 1. Clone the Repository

```bash
git clone https://github.com/Vengatesh12/wordpress-gitops-k8s.git
cd wordpress-gitops-k8s
```

### 2. Setup Argo CD in Your Cluster

> Ensure Argo CD is installed and accessible.

```bash
kubectl create namespace argocd
# Apply Argo CD manifests (or use Helm)
```

### 3. Create Namespaces

```bash
kubectl create ns nginx
kubectl create ns wp
kubectl create ns db
```

### 4. Apply Argo CD App CRDs

```bash
kubectl apply -f argocd/
```

### 5. Push Changes to Trigger GitOps

Update values in Helm charts or image tags in the repository, then commit and push:

```bash
git add .
git commit -m "Update image tag for WordPress"
git push
```

Argo CD will detect the change and automatically apply the new configuration.

---

## 🔐 Security Practices

- Secrets are encrypted using tools like **SOPS** or **SealedSecrets**.
- Only Nginx is exposed to the public (via `NodePort` or `Ingress`).
- Internal components (WordPress and DB) are only accessible within the cluster.

---

## 🏷️ Kubernetes Labels

All resources are tagged with the following labels:

```yaml
labels:
  id: <your-college-id>
  app: <name-of-the-app>
  env: dev
```

---




