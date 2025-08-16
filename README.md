# 🚀 Kubernetes Automation CLI Tool

## Overview
This CLI tool automates operations on a Kubernetes cluster, including:

- Connecting to the cluster
- Installing Helm and KEDA
- Deploying applications with autoscaling
- Checking deployment health and metrics

## ✨ Features
- 🔧 Connects to Kubernetes via `kubectl`
- 📦 Installs Helm and KEDA
- 🚀 Deploys apps with event-driven autoscaling
- 📊 Retrieves deployment health and resource usage
- 🧱 Modular and extensible CLI using Python + Click

---

## 📦 Prerequisites

- Kubernetes cluster (e.g., Docker Desktop with Kubernetes enabled)
- Python 3.8+
- Helm installed
- kubectl installed and configured

---

## 🛠️ Installation

```bash
cd k8s_automation
python -m venv venv
venv\Scripts\activate           # For Windows
pip install -r requirements.txt
```
---

## Usage
# 1.Install KEDA (Kubernetes Event-Driven Autoscaling)
```bash
python k8s_automation.py install-keda
```
Installs KEDA using Helm into the keda namespace.

# 2. Deploy an Application

```bash
python k8s_automation.py deploy \
  --name myapp \
  --namespace default \
  --image nginx:latest \
  --cpu-request 100m \
  --cpu-limit 200m \
  --memory-request 128Mi \
  --memory-limit 256Mi \
  --port 80 \
  --min-replicas 1 \
  --max-replicas 5 \
  --target-cpu 50
 ```
 Deploys an app with KEDA-based autoscaling.
 ## 3. Check Deployment Health
 ```bash 
 python k8s_automation.py health --namespace default --name myapp
 ```
 Returns pod status, CPU/memory usage (metrics-server required).

## 🧩Design Overview

🧱 Modularity:
Each function is isolated for reuse and testing.

🔘 CLI Interface:
Uses Click for a clean, user-friendly CLI.

⚙️ KEDA Integration:
Installs KEDA and allows autoscaling using custom event metrics.

🛡️ Error Handling:
Handles missing tools, misconfigured clusters, and invalid configs.

🔍 Validation:
Validates cluster connection and existing resources before proceeding.

---

### Screenshots / Logs

## KEDA Installation:
```bash 
 python k8s_automation.py install-keda
 ```
This screenshot shows successful installation of KEDA on the cluster.
<img width="1920" height="1008" alt="Keda-installation" src="https://github.com/user-attachments/assets/b8fd4bb9-3640-43a6-8d2b-7dbbc86a6345" />

![KEDA Installation](./Screenshots/keda-installation.png)
---

## Deployment Success
```bash
 python k8s_automation.py deploy --name myapp --namespace default --image nginx:latest --cpu-request 100m --cpu-limit 200m --memory-request 128Mi --memory-limit 256Mi --port 80 --min-replicas 1 --max-replicas 5 --target-cpu 50
```
Below is the output from the CLI when deploying the application.
![Deployment Success](./screenshots/deployment-success.png)

---

##  Health Status Check
``` bash 
 python k8s_automation.py status --name myapp --namespace default
```
Here we check the health status of the deployed application.
![Health Check](./screenshots/health-check.png)


### Get Kubernetes Resource Details
``` bash
kubectl get deployments -n default
kubectl get pods -n default -l app=myapp
kubectl get hpa -n default
```
![Resouces](./screenshots/resources.png)

###  Check logs of specific pods
```bash
 kubectl logs myapp-667ff8d48f-mbks9 -n default
 ```

![Pod Logs](./screenshots/logs.png)
