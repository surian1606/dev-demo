import boto3

client = boto3.client('dynamodb')

response = client.delete_table(
    TableName='Daftar-Tak-Hadir'
)