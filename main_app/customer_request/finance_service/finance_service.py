import json


def lambda_handler(event, context):
    try:
        # Retrieve request body from event
        body = event['body']

        # Do some processing here...

        # Return a response
        response = {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json'
            },
            'body': json.dumps({'message': 'Success'})
        }

    except Exception as e:
        # Handle any exceptions that occur during processing
        response = {
            'statusCode': 500,
            'headers': {
                'Content-Type': 'application/json'
            },
            'body': json.dumps({'message': 'Error: ' + str(e)})
        }

    # Return the response to the caller
    return response
