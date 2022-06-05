from http import client
import boto3

client = boto3.client('dynamodb')

response = client.create_table(
    AttributeDefinitions=[
        {
            'AttributeName': 'Nama',
            'AttributeType': 'S'
        },
    ],
    TableName='Daftar-Hadir',
    KeySchema=[
        {
            'AttributeName': 'Nama',
            'KeyType': 'HASH'
        },
    ],
    BillingMode='PAY_PER_REQUEST',
    TableClass='STANDARD'
)