# dynamodb.py
from __future__ import print_function
import boto3

dynamodb = boto3.resource('dynamodb', region_name='eu-west-2', endpoint_url="http://localhost:8000")

table = dynamodb.create_table(
    TableName='Login',
    KeySchema=[
        {
            'AttributeName': 'username',
            'KeyType': 'HASH'  #Partition key
        },
        {
            'AttributeName': 'password',
            'KeyType': 'RANGE'  #Sort key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'username',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'password',
            'AttributeType': 'S'
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
)

print("Table status:", table.table_status)
