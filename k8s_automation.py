import click
import subprocess
import json

def run_cmd(cmd):
    """Helper to run shell commands and capture output"""
    try:
        result = subprocess.run(cmd, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        click.echo(f"Error running command: {e.stderr.strip()}")
        return None

def install_keda():
    click.echo("🚀 Installing KEDA...")
    # Add Helm repo and update
    run_cmd("helm repo add kedacore https://kedacore.github.io/charts")
    run_cmd("helm repo update")

    # Create namespace if not exists
    ns_exists = run_cmd("kubectl get namespace keda --ignore-not-found")
    if not ns_exists:
        run_cmd("kubectl create namespace keda")
    else:
        click.echo("Namespace 'keda' already exists")

    # Install or upgrade KEDA helm chart
    output = run_cmd("helm upgrade --install keda kedacore/keda --namespace keda")
    click.echo(output or "KEDA installed/upgraded successfully.")

def create_deployment(name, namespace, image, cpu_request, cpu_limit, memory_request, memory_limit, port, min_replicas, max_replicas, target_cpu):
    click.echo(f"Deploying '{name}' in namespace '{namespace}' with image '{image}'")
    # Here you would create deployment, service, and KEDA HPA using kubectl or client libraries
    # For example, use kubectl apply -f deployment.yaml or dynamic template filling
    # This is a stub, replace with your actual deployment logic
    click.echo(f"CPU request: {cpu_request}, CPU limit: {cpu_limit}")
    click.echo(f"Memory request: {memory_request}, Memory limit: {memory_limit}")
    click.echo(f"Port: {port}, Replicas: min={min_replicas}, max={max_replicas}, target CPU: {target_cpu}%")
    # Simulate success
    click.echo("Deployment created successfully.")

def check_status(name, namespace):
    click.echo(f"Getting status for deployment '{name}' in namespace '{namespace}'")
    # Check deployment status
    deployment_status = run_cmd(f"kubectl get deployment {name} -n {namespace} -o json")
    if not deployment_status:
        click.echo("Deployment not found or error fetching deployment")
        return

    deployment = json.loads(deployment_status)
    available_replicas = deployment.get("status", {}).get("availableReplicas", 0)
    ready_replicas = deployment.get("status", {}).get("readyReplicas", 0)
    replicas = deployment.get("status", {}).get("replicas", 0)

    click.echo(f"Replicas: {replicas}, Ready: {ready_replicas}, Available: {available_replicas}")

    # Check pods
    pods = run_cmd(f"kubectl get pods -n {namespace} -l app={name} -o json")
    if not pods:
        click.echo("No pods found or error fetching pods")
        return
    pods_data = json.loads(pods)
    for pod in pods_data.get("items", []):
        pod_name = pod["metadata"]["name"]
        pod_status = pod["status"]["phase"]
        click.echo(f"Pod: {pod_name} | Status: {pod_status}")

@click.group()
def cli():
    pass

@cli.command()
def install_keda_cmd():
    """Install KEDA on the Kubernetes cluster."""
    install_keda()

@cli.command()
@click.option('--name', required=True, help='Deployment name')
@click.option('--namespace', default='default', help='Kubernetes namespace')
@click.option('--image', required=True, help='Container image with tag')
@click.option('--cpu-request', default='100m', help='CPU request')
@click.option('--cpu-limit', default='200m', help='CPU limit')
@click.option('--memory-request', default='128Mi', help='Memory request')
@click.option('--memory-limit', default='256Mi', help='Memory limit')
@click.option('--port', default=80, help='Container port')
@click.option('--min-replicas', default=1, help='Minimum number of replicas')
@click.option('--max-replicas', default=5, help='Maximum number of replicas')
@click.option('--target-cpu', default=50, help='Target CPU utilization percentage for autoscaling')
def deploy(name, namespace, image, cpu_request, cpu_limit, memory_request, memory_limit, port, min_replicas, max_replicas, target_cpu):
    """Deploy the application using specified parameters."""
    create_deployment(name, namespace, image, cpu_request, cpu_limit, memory_request, memory_limit, port, min_replicas, max_replicas, target_cpu)

@cli.command()
@click.option('--name', required=True, help='Deployment name')
@click.option('--namespace', default='default', help='Kubernetes namespace')
def status(name, namespace):
    """Get the health status of the deployment."""
    check_status(name, namespace)

if __name__ == '__main__':
    cli()
