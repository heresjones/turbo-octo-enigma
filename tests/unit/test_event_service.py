import json

import pytest

import main_app.customer_request.event_service.event_service as event_service
import main_app.customer_request.event_service.event_service as app


def test_bad_response():
    response = event_service.lambda_handler(None, None)
    assert response['statusCode'] == 400


# def test_good_response(request_event_example):
#     response = json.loads(event_service.lambda_handler(request_event_example, None))
#     print("Response", response)
#     assert response['statusCode'] == 200

def test_api_event(api_event):
    response = json.loads(event_service.lambda_handler(api_event, None))
    assert response['statusCode'] == 200


def test_get_event(api_event):
    test_body = json.loads(api_event["body"])
    get_event_response_body = json.loads(event_service.get_event(test_body["body"]))
    test_body = json.loads(api_event["body"])
    assert get_event_response_body['body']['eventId'] == test_body["body"]['eventId']


def test_error_400():
    message = 'Invalid input'
    response = event_service.error_400(message)
    assert response['statusCode'] == 400
    assert response['body'] == message



@pytest.fixture()
def event_example():
    return {
        "eventId": "123456",
        "eventName": "Live concert",
        "eventDate": "2023-06-01",
        "eventTime": "19:00",
        "eventLocation": {
            "name": "Venue Name",
            "address": "123 Main Street, Anytown USA"
        },
        "eventDescription": "Join us for a live concert featuring amazing artists!",
        "eventPhoto": {
            "s3Bucket": "my-event-photos",
            "s3Key": "123456.jpg"
        },
        "artistWebsite": "https://www.example.com/artist",
        "potentialWebsites": [
            "https://www.example.com",
            "https://www.anotherexample.com"
        ],
        "artists": [
            {
                "name": "Artist 1",
                "genre": "Rock"
            },
            {
                "name": "Artist 2",
                "genre": "Pop"
            }
        ]
    }


@pytest.fixture()
def api_event():
    return {'resource': '/event', 'path': '/event', 'httpMethod': 'POST', 'headers': None, 'multiValueHeaders': None,
            'queryStringParameters': None, 'multiValueQueryStringParameters': None, 'pathParameters': None,
            'stageVariables': None,
            'requestContext': {'resourceId': '914dl8', 'resourcePath': '/event', 'httpMethod': 'POST',
                               'extendedRequestId': 'AnjrIHHNIAMFQ2w=', 'requestTime': '20/Feb/2023:03:17:26 +0000',
                               'path': '/event', 'accountId': '208827447334', 'protocol': 'HTTP/1.1',
                               'stage': 'test-invoke-stage', 'domainPrefix': 'testPrefix',
                               'requestTimeEpoch': 1676863046958, 'requestId': '33a1b2c5-2389-4efa-98a4-59886eb8b8d7',
                               'identity': {'cognitoIdentityPoolId': None, 'cognitoIdentityId': None,
                                            'apiKey': 'test-invoke-api-key', 'principalOrgId': None,
                                            'cognitoAuthenticationType': None,
                                            'userArn': 'arn:aws:iam::208827447334:root',
                                            'apiKeyId': 'test-invoke-api-key-id',
                                            'userAgent': 'aws-internal/3 aws-sdk-java/1.12.401 Linux/5.4.228-141.415.amzn2int.x86_64 OpenJDK_64-Bit_Server_VM/25.362-b09 java/1.8.0_362 vendor/Oracle_Corporation cfg/retry-mode/standard',
                                            'accountId': '208827447334', 'caller': '208827447334',
                                            'sourceIp': 'test-invoke-source-ip', 'accessKey': 'ASIATBHYV7ATC5QYWRGE',
                                            'cognitoAuthenticationProvider': None, 'user': '208827447334'},
                               'domainName': 'testPrefix.testDomainName', 'apiId': 'ny0jv08tc3'},
            'body': '{\r\n        "body": {\r\n            "eventType": "getEvent",\r\n            "eventId": '
                    '"123456",\r\n            "mode": "test"\r\n        }\r\n    }',
            'isBase64Encoded': False}


# import json
# import os
# from unittest import mock
# import boto3
# from botocore.exceptions import ClientError
# import pytest
#
#
#
# # Test data
# test_event_id = '1234'
# test_event_body = {
#     'eventType': 'getEvent',
#     'eventId': test_event_id,
#     'mode': 'test'
# }
# test_event = {
#     'eventId': test_event_id,
#     'eventName': 'Test Event',
#     'eventDate': '2023-03-15',
#     'eventTime': '12:00 PM',
#     'eventLocation': {
#         'name': 'Test Venue',
#         'address': '123 Test St.'
#     },
#     'eventDescription': 'This is a test event',
#     'eventPhoto': {
#         's3Bucket': 'test-bucket',
#         's3Key': 'test-photo.jpg'
#     },
#     'artistWebsite': 'http://www.example.com',
#     'potentialWebsites': ['http://www.example.com', 'http://www.test.com'],
#     'artists': [
#         {'name': 'Test Artist 1', 'genre': 'Rock'},
#         {'name': 'Test Artist 2', 'genre': 'Pop'}
#     ]
# }
#
#
# def mock_query_event_table(event_id):
#     # Mock the DynamoDB table response
#     return test_event
#
#
# def test_lambda_handler_get_event():
#     # Test the getEvent event type
#     event = {
#         'body': json.dumps(test_event_body)
#     }
#
#     with mock.patch.object(boto3, 'resource') as mock_dynamodb:
#         mock_table = mock.MagicMock()
#         mock_table.get_item.side_effect = mock_query_event_table
#         mock_dynamodb.return_value.Table.return_value = mock_table
#
#         response = app.lambda_handler(event, {})
#         response_body = json.loads(response['body'])
#
#         assert response['statusCode'] == 200
#         assert response_body == test_event
#
#
# def test_lambda_handler_search_events():
#     # Test the searchEvents event type
#     event = {
#         'body': json.dumps({
#             'eventType': 'searchEvents',
#             'query': 'test'
#         })
#     }
#
#     response = app.lambda_handler(event, {})
#
#     assert response['statusCode'] == 400
#     assert 'Invalid input: missing query' in response['body']
#
#
# def test_lambda_handler_missing_event_type():
#     # Test the case where the eventType is missing
#     event = {
#         'body': json.dumps({
#             'eventId': test_event_id,
#             'mode': 'test'
#         })
#     }
#
#     response = app.lambda_handler(event, {})
#
#     assert response['statusCode'] == 400
#     assert 'Invalid input: missing eventType' in response['body']
#
#
# def test_lambda_handler_missing_event_id():
#     # Test the case where the eventId is missing for the getEvent event type
#     event = {
#         'body': json.dumps({
#             'eventType': 'getEvent',
#             'mode': 'test'
#         })
#     }
#
#     response = app.lambda_handler(event, {})
#
#     assert response['statusCode'] == 400
#     assert 'Invalid input: missing eventId' in response['body']
#
#
# def test_lambda_handler_invalid_event_type():
#     # Test the case where the eventType is invalid
#     event = {
#         'body': json.dumps({
#             'eventType': 'invalid'
#         })
#     }
#
#     response = app.lambda_handler(event, {})
#
#     assert response['statusCode'] == 400
#     assert 'Invalid input: unknown eventType' in response['body']
