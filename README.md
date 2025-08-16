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

---

## Deployment Success
```bash
 python k8s_automation.py deploy --name myapp --namespace default --image nginx:latest --cpu-request 100m --cpu-limit 200m --memory-request 128Mi --memory-limit 256Mi --port 80 --min-replicas 1 --max-replicas 5 --target-cpu 50
```
Below is the output from the CLI when deploying the application.
<img width="1895" height="246" alt="deployment-success" src="https://github.com/user-attachments/assets/923e10ef-44d0-47fd-8d74-0c94302568cf" />

---

##  Health Status Check
``` bash 
 python k8s_automation.py status --name myapp --namespace default
```
Here we check the health status of the deployed application.
<img width="1902" height="167" alt="health-check" src="https://github.com/user-attachments/assets/6680bfe8-1d08-432e-b38a-a5fa531543d8" />


### Get Kubernetes Resource Details
``` bash
kubectl get deployments -n default
kubectl get pods -n default -l app=myapp
kubectl get hpa -n default
```
<img width="1559" height="336" alt="resources" src="https://github.com/user-attachments/assets/bd50330c-ad74-4554-ae62-8e46b00e6ebe" />

###  Check logs of specific pods
```bash
 kubectl logs myapp-667ff8d48f-mbks9 -n default
 ```

<img width="1920" height="1008" alt="logs" src="https://github.com/user-attachments/assets/17d0ec54-a521-43c5-b1a6-63ee67ed4e6d" />

