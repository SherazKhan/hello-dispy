"""
Launch EC2 instances.
"""

import sys
import boto3
import coils

config = coils.Config('ec2.conf')

ec2 = boto3.resource(
    'ec2',
    region_name=config['region'],
    aws_access_key_id=config['access_key_id'],
    aws_secret_access_key=config['secret_access_key'],
)

instances = ec2.create_instances(
    #DryRun=True,
    ImageId=config['ami_id'],
    InstanceType=config['instance_type'],
    MinCount=int(config['instance_count']),
    MaxCount=int(config['instance_count']),
)

for index, instance in enumerate(instances):
    instance.create_tags(Tags=[{'Key':'Name', 'Value':'dispy.{}'.format(index)}])
