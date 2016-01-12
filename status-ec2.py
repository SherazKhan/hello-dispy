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

instances = list()
for instance_id in instance_ids:
    instance = ec2.Instance(instance_id)
    instances.append(instance)

print('id  name  public_ip')
print('--  ----  ---------')
for instance in instances:
    print('{}  {}  {}'.format(instance.id, instance.tags[0]['Value'], instance.public_ip_address))
