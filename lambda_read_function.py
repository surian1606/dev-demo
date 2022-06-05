import boto3
from datetime import datetime


sts_client = boto3.client('sts')
sts_session = sts_client.assume_role(RoleArn='arn:aws:iam::<Account-A ID>::role/DynamoDB-FullAccess-For-Account-B',
                                      RoleSessionName='test-dynamodb-session')


KEY_ID = sts_session['Credentials']['AccessKeyId']
ACCESS_KEY = sts_session['Credentials']['SecretAccessKey']
TOKEN = sts_session['Credentials']['SessionToken']


dynamodb_client = boto3.client('dynamodb',
                                region_name='us-east-2',
                                aws_access_key_id=KEY_ID,
                                aws_secret_access_key=ACCESS_KEY,
                                aws_session_token=TOKEN)


def lambda_handler(event, context):
    response = dynamodb_client.get_item(TableName='Table-Acccount-A', Key={'category':{'S':'Fruit'}, 'item':{'S':'Apple'}})


    return response
