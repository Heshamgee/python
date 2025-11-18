import requests
import subprocess
import sys
import os

class CICDPipeline:
    def __init__(self, repo_url, webhook_url=None):
        self.repo_url = repo_url
        self.webhook_url = webhook_url
    
    def run_tests(self):
        """Run application tests"""
        try:
            result = subprocess.run(
                ['pytest', 'tests/', '--junitxml=test-results.xml'],
                capture_output=True,
                text=True
            )
            return result.returncode == 0
        except Exception as e:
            print(f"Test execution failed: {e}")
            return False
    
    def build_project(self):
        """Build the project"""
        try:
            # Example: Build a Python package
            subprocess.run(['python', 'setup.py', 'sdist', 'bdist_wheel'], check=True)
            print("Build completed successfully")
            return True
        except subprocess.CalledProcessError as e:
            print(f"Build failed: {e}")
            return False
    
    def deploy(self, environment='staging'):
        """Deploy to specified environment"""
        deploy_scripts = {
            'staging': './deploy-staging.sh',
            'production': './deploy-production.sh'
        }
        
        script = deploy_scripts.get(environment)
        if script and os.path.exists(script):
            subprocess.run(['bash', script], check=True)
            print(f"Deployed to {environment} successfully")
            return True
        return False
    
    def send_notification(self, message, status):
        """Send notification via webhook"""
        if self.webhook_url:
            payload = {
                'text': f'{message} - Status: {status}',
                'status': status
            }
            try:
                requests.post(self.webhook_url, json=payload)
            except Exception as e:
                print(f"Notification failed: {e}")
    
    def run_pipeline(self):
        """Execute complete CI/CD pipeline"""
        print("Starting CI/CD Pipeline...")
        
        # Run tests
        if not self.run_tests():
            self.send_notification("Tests failed", "FAILED")
            sys.exit(1)
        
        # Build project
        if not self.build_project():
            self.send_notification("Build failed", "FAILED")
            sys.exit(1)
        
        # Deploy to staging
        if self.deploy('staging'):
            self.send_notification("Deployed to staging", "SUCCESS")
        else:
            self.send_notification("Staging deployment failed", "FAILED")
            sys.exit(1)

# Usage
pipeline = CICDPipeline(
    repo_url="https://github.com/your-repo",
    webhook_url="https://hooks.slack.com/your-webhook"
)
pipeline.run_pipeline()
