import json
import boto3

iam_client = boto3.client('iam')

paginator = iam_client.get_paginator('list_roles')

aws_roles = []

for page in paginator.paginate():
#    print(json.dumps(page, indent=4, default=str), "\n\n")
    for role in page['Roles']:
        aws_roles.append(role['RoleName'])

print('\n'.join(aws_roles))