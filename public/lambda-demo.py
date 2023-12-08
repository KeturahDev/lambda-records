import json
import boto3
from uuid import uuid4
from random import randint
from boto3.dynamodb.conditions import Key, Attr
from time import gmtime, strftime

dynamodb = boto3.resource('dynamodb')
table_demo = dynamodb.Table('table-demo')

def lambda_handler(event, context):
    name_value = "no-name" if 'queryStringParameters' not in event else event['queryStringParameters'].get('name', None)
    color_value = "transparent" if 'queryStringParameters' not in event else event['queryStringParameters'].get('color', "white")
    now = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())

        # response = users_table.get_item(Key={'user': user_value})
    
    newline = {
        "id": str(uuid4()), 
        "name": name_value,
        "color": color_value,
        "power": randint(0, 20),
        "date": now,
    }
    demo_response = table_demo.put_item(Item=newline)
    print("log----", name_value, color_value, now)
    return {
        'statusCode': demo_response['ResponseMetadata']['HTTPStatusCode'],
        'body': json.dumps(newline)
    }
