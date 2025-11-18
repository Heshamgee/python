import boto3
import json

class EC2Manager:
    def __init__(self):
        self.ec2 = boto3.client('ec2')
        self.ec2_resource = boto3.resource('ec2')
    
    def list_instances(self):
        """List all EC2 instances"""
        response = self.ec2.describe_instances()
        instances = []
        
        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                instances.append({
                    'InstanceId': instance['InstanceId'],
                    'State': instance['State']['Name'],
                    'Type': instance['InstanceType'],
                    'LaunchTime': instance['LaunchTime']
                })
        
        return instances
    
    def start_instance(self, instance_id):
        """Start a specific EC2 instance"""
        response = self.ec2.start_instances(InstanceIds=[instance_id])
        return response
    
    def create_instance(self, image_id='ami-0c02fb55956c7d316', instance_type='t2.micro'):
        """Create a new EC2 instance"""
        response = self.ec2.run_instances(
            ImageId=image_id,
            InstanceType=instance_type,
            MinCount=1,
            MaxCount=1,
            TagSpecifications=[{
                'ResourceType': 'instance',
                'Tags': [{'Key': 'Name', 'Value': 'Python-Created-Instance'}]
            }]
        )
        return response['Instances'][0]['InstanceId']

# Usage
if __name__ == "__main__":
    manager = EC2Manager()
    print("Current instances:", manager.list_instances())
