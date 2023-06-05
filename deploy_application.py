import os
import subprocess
import time
import json
print('Deploy script started')
# Define the root directory and k8sconfig directory
root_dir = os.path.dirname(os.getcwd())
k8sconfig_dir = os.path.join(root_dir, 'k8sconfig')
print(f'root_dir is {root_dir}')
print(f'k8sconfig_dir is {k8sconfig_dir}')
subprocess.check_call(["minikube", "addons", "enable","ingress"])
subprocess.check_call(["minikube", "addons", "enable","ingress-dns"])
# Read the microservices from a JSON file
with open('config.json', 'r') as f:
    data = json.load(f)
    microservices = data['microservices']  # The JSON file should have a "microservices" key

for microservice in microservices:
    print(f'we are at the microservice: {microservice}')
    # Apply volume and config .yml files for each microservice in the k8sconfig directory
    for file_name in ['volume.yml', 'config.yml']:
        file_path = os.path.join(k8sconfig_dir, microservice, file_name)
        
        if os.path.isfile(file_path):
            try:
                print(f'   microservice: {microservice} file_path is {file_path} exists')
                subprocess.check_call(['kubectl', 'apply', '-f', file_path])
                if file_name == 'volume.yml':  # if it's a volume configuration, add a delay
                    time.sleep(10)  # sleep for 10 seconds
            except subprocess.CalledProcessError:
                print(f'Failed to apply {file_name} for microservice {microservice}')
    
    # Check if there's a directory for the microservice and if it has a skaffold.yaml file
    microservice_dir = os.path.join(root_dir, microservice)
    if os.path.isdir(microservice_dir) and os.path.isfile(os.path.join(microservice_dir, 'skaffold.yaml')):
        try:
            os.chdir(microservice_dir)
            subprocess.check_call(['skaffold', 'run'])
        except subprocess.CalledProcessError:
            print(f'Skaffold failed for microservice {microservice}')
    else:  # If no skaffold file, apply the deployment configuration
        deployment_file = os.path.join(k8sconfig_dir, microservice, 'deployment.yml')
        if os.path.isfile(deployment_file):
            try:
                subprocess.check_call(['kubectl', 'apply', '-f', deployment_file])
            except subprocess.CalledProcessError:
                print(f'Failed to apply deployment for microservice {microservice}')
subprocess.check_call(["kubectl", "apply", "-k", "../k8sconfig/ingress"])
subprocess.check_call(["kubectl", "apply", "-f", "../k8sconfig/ingress/ingress.yaml"])
subprocess.check_call(["kubectl", "rollout", "restart", "-n", "ingress-nginx", "deployment", "ingress-nginx-controller"])
print('done')
