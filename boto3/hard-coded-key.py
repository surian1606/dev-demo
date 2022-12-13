import boto3

ACCESS_KEY='AKIAW777UUPYIPHJI7GS'
SECRET_KEY='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'

s3 = boto3.client(
    's3',
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY
    )
response = s3.list_buckets()

print('Existing buckets:')
for bucket in response['Buckets']:
    print(f'  {bucket["Name"]}')
