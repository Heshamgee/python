import docker
import subprocess
import json

class DockerManager:
    def __init__(self):
        self.client = docker.from_client()
    
    def list_containers(self, all_containers=False):
        """List all containers"""
        containers = self.client.containers.list(all=all_containers)
        return [{'id': container.id, 'name': container.name, 'status': container.status} 
                for container in containers]
    
    def build_image(self, dockerfile_path, tag):
        """Build Docker image"""
        try:
            image, logs = self.client.images.build(
                path=dockerfile_path,
                tag=tag,
                rm=True
            )
            print(f"Image built successfully: {tag}")
            return image
        except docker.errors.BuildError as e:
            print(f"Build failed: {e}")
            return None
    
    def run_container(self, image, ports=None, environment=None):
        """Run a container"""
        container = self.client.containers.run(
            image,
            detach=True,
            ports=ports or {},
            environment=environment or {}
        )
        return container.id

# Usage
docker_manager = DockerManager()
print("Running containers:", docker_manager.list_containers())
