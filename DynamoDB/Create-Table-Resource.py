import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.create_table(
    AttributeDefinitions=[
        {
            'AttributeName': 'Nama',
            'AttributeType': 'S'
        },
    ],
    TableName='Daftar-Tak-Hadir',
    KeySchema=[
        {
            'AttributeName': 'Nama',
            'KeyType': 'HASH'
        },
    ],
    BillingMode='PAY_PER_REQUEST',
    TableClass='STANDARD'
)