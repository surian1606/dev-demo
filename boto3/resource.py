import boto3

iam_resource = boto3.resource('iam')

aws_roles = []

for role in iam_resource.roles.all():
    aws_roles.append(role.name)

print('\n'.join(aws_roles))