import os
import subprocess
import json

def load_branches(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data["branches"]

def clone_repo_for_branches(branches):
    url = "git@github.com:adriandborsan/web-app-spring-boot.git"
    parent_dir = os.path.dirname(os.getcwd())
    for branch in branches:
        directory = os.path.join(parent_dir, branch)
        try:
            # Check if directory already exists.
            if os.path.exists(directory):
                print(f"Directory {directory} already exists. Skipping...")
                continue
            # clone the specific branch into a directory named after the branch
            subprocess.check_call(["git", "clone", "--single-branch", "--branch", branch, url, directory])
            print(f"Successfully cloned branch {branch} into {directory}")
        except subprocess.CalledProcessError as e:
            print(f"Failed to clone branch {branch} into {directory}. Error: {e}")

if __name__ == "__main__":
    branches = load_branches("config.json")
    clone_repo_for_branches(branches)
