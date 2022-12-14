import boto3

##Remove the comment for using hard-coded credentials
#ACCESS_KEY='<your-access-key-id-here>'
#SECRET_KEY='<your-secret-access-key-here>'

s3 = boto3.client(
    's3'#,
    #aws_access_key_id=ACCESS_KEY,
    #aws_secret_access_key=SECRET_KEY
    )

#To use custom profile, please use below snippet instead
#s3 = boto3.session.Session(profile_name='developer').client('s3')

response = s3.list_buckets()

print('Existing buckets:')
for bucket in response['Buckets']:
    print(f'  {bucket["Name"]}')