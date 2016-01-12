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

with open('ids.txt', 'r') as ff:
    instance_ids = [line.strip() for line in ff.readlines()]

for instance_id in instance_ids:
    print(instance_id)

ec2.instances.filter(InstanceIds=instance_ids).terminate()
