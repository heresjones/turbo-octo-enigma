import json
import boto3
import os
from botocore.exceptions import ClientError


def lambda_handler(event, context):

    if not isinstance(event, dict):
        return error_400('Invalid input: event must be a dict')

    if event is None or 'body' not in event:
        return error_400('Invalid input: missing body')
    body = event['body']

    # Convert API GATEWAY RESPONSE [body] to a dict
    if isinstance(body, str):
        try:
            body = json.loads(event['body'])
        except BaseException as e:
            return error_400('Invalid input: event body must be a dict')


    if 'eventType' not in body:
        return error_400('Invalid input: missing eventType')

    event_type = body['eventType']

    if event_type == 'getEvent':
        if 'eventId' not in body:
            return error_400('Invalid input: missing eventId')
        return get_event(body)
    elif event_type == 'searchEvents':
        if 'query' not in body:
            return error_400('Invalid input: missing query')
        return search_events(event)
    else:
        return error_400('Invalid input: unknown eventType')


def error_400(message):
    return {
        'statusCode': 400,
        "isBase64Encoded": False,
        'body': message
    }


def get_event(body):
    event_id = body['eventId']

    if body['mode'] != 'test':
        return json.dumps(query_event_table(event_id))
    else:
        # Construct the path to the event file using the unit test directory
        file_path = os.path.join(os.getcwd(), 'event.json')
        with open(file_path, 'r') as f:
            file_contents = json.loads(f.read())
            response = {
                'statusCode': 200,
                'headers': {
                    'Content-Type': 'application/json'
                },
                'body': file_contents,
                "isBase64Encoded": False
            }
            return json.dumps(response)


def query_event_table(event_id):
    dynamodb = boto3.resource('dynamodb')
    table_name = 'event-table'

    try:
        table = dynamodb.Table(table_name)
        response = table.get_item(
            Key={
                'eventId': event_id
            }
        )
        item = response.get('Item')
        if item:
            response = {
                'statusCode': 200,
                'headers': {
                    'Content-Type': 'application/json'
                },
                'body': item,
                "isBase64Encoded": False
            }
            return json.dumps(response)
        else:
            raise Exception(f"Event with ID {event_id} not found.")
    except ClientError as e:
        return {
            'statusCode': 400,
            "isBase64Encoded": False,
            'body': f"Event with ID {event_id} not found."
        }


# add event to dynamoDB table
def add_event(new_event):
    dynamodb = boto3.resource('dynamodb')
    table_name = 'event-table'
    table = dynamodb.Table(table_name)

    try:
        response = table.put_item(
            Item={
                'eventId': new_event['eventId'],
                'eventName': new_event['eventName'],
                'eventDate': new_event['eventDate'],
                'eventTime': new_event['eventTime'],
                'eventLocation': new_event['eventLocation'],
                'eventDescription': new_event['eventDescription'],
                'eventPhoto': new_event['eventPhoto'],
                'artistWebsite': new_event['artistWebsite'],
                'potentialWebsites': new_event['potentialWebsites'],
                'artists': new_event['artists']
            }
        )
        response = {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json'
            },
            'body': json.dumps(response),
            "isBase64Encoded": False
        }
        return json.dumps(response)
    except ClientError as e:
        return {
            'statusCode': 400,
            "isBase64Encoded": False,
            'body': f"Failed to put event with ID {new_event['eventId']}. Error: {e.response['Error']['Message']}"
        }


# Todo Search
def search_events(query):
    pass
