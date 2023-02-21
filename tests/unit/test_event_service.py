import json

import pytest

import main_app.customer_request.event_service.event_service as event_service


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


# def test_get_event(api_event):
#     test_body = json.loads(api_event)
#     print("TEST BODY", type(test_body), test_body)
#     get_event_response_body = json.loads(event_service.get_event(test_body["body"]))
#     test_body = json.loads(api_event["body"])
#     assert get_event_response_body['body']['eventId'] == test_body['eventId']


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
            'requestContext': {'resourceId': 'pukd69', 'resourcePath': '/event', 'httpMethod': 'POST',
                               'extendedRequestId': 'AqHM-EhmIAMFbMQ=', 'requestTime': '20/Feb/2023:21:53:48 +0000',
                               'path': '/event', 'accountId': '208827447334', 'protocol': 'HTTP/1.1',
                               'stage': 'test-invoke-stage', 'domainPrefix': 'testPrefix',
                               'requestTimeEpoch': 1676930028381, 'requestId': '58b87da5-287a-45e1-b91a-2bfdc0d61471',
                               'identity': {'cognitoIdentityPoolId': None, 'cognitoIdentityId': None,
                                            'apiKey': 'test-invoke-api-key', 'principalOrgId': None,
                                            'cognitoAuthenticationType': None,
                                            'userArn': 'arn:aws:iam::208827447334:root',
                                            'apiKeyId': 'test-invoke-api-key-id',
                                            'userAgent': 'aws-internal/3 aws-sdk-java/1.12.406 Linux/5.4.228-141.415.amzn2int.x86_64 OpenJDK_64-Bit_Server_VM/25.362-b10 java/1.8.0_362 vendor/Oracle_Corporation cfg/retry-mode/standard',
                                            'accountId': '208827447334', 'caller': '208827447334',
                                            'sourceIp': 'test-invoke-source-ip', 'accessKey': 'ASIATBHYV7ATHLE2RZN5',
                                            'cognitoAuthenticationProvider': None, 'user': '208827447334'},
                               'domainName': 'testPrefix.testDomainName', 'apiId': 'acm0ux17e7'},
            'body': '{\r\n    "eventType": "getEvent",\r\n    "eventId": "123456",\r\n    "mode": "test"\r\n}',
            'isBase64Encoded': False}


@pytest.fixture()
def postman_event():
    return {'resource': '/event', 'path': '/event', 'httpMethod': 'POST',
            'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate, br',
                        'Authorization': 'Bearer a9pyY9M4SHd4SEqvaApQ', 'CloudFront-Forwarded-Proto': 'https',
                        'CloudFront-Is-Desktop-Viewer': 'true', 'CloudFront-Is-Mobile-Viewer': 'false',
                        'CloudFront-Is-SmartTV-Viewer': 'false', 'CloudFront-Is-Tablet-Viewer': 'false',
                        'CloudFront-Viewer-ASN': '7922', 'CloudFront-Viewer-Country': 'US',
                        'Content-Type': 'application/json', 'Host': 'acm0ux17e7.execute-api.us-east-1.amazonaws.com',
                        'Postman-Token': 'b30be14f-d1ce-47fe-b68d-0a272200cac5', 'User-Agent': 'PostmanRuntime/7.31.0',
                        'Via': '1.1 95edb2a6efdb5ee4d3c7f7aa298bb2f2.cloudfront.net (CloudFront)',
                        'X-Amz-Cf-Id': 'Du8C80Yb59Mbb-ReCPO2i2qmZm6epLm87ZK4yf_ytUlwFeFAJzg6Dw==',
                        'X-Amzn-Trace-Id': 'Root=1-63f3f66c-453eb11b265c5ea13e8523f4',
                        'X-Forwarded-For': '98.216.16.152, 130.176.166.15', 'X-Forwarded-Port': '443',
                        'X-Forwarded-Proto': 'https'},
            'multiValueHeaders': {'Accept': ['*/*'], 'Accept-Encoding': ['gzip, deflate, br'],
                                  'Authorization': ['Bearer a9pyY9M4SHd4SEqvaApQ'],
                                  'CloudFront-Forwarded-Proto': ['https'], 'CloudFront-Is-Desktop-Viewer': ['true'],
                                  'CloudFront-Is-Mobile-Viewer': ['false'], 'CloudFront-Is-SmartTV-Viewer': ['false'],
                                  'CloudFront-Is-Tablet-Viewer': ['false'], 'CloudFront-Viewer-ASN': ['7922'],
                                  'CloudFront-Viewer-Country': ['US'], 'Content-Type': ['application/json'],
                                  'Host': ['acm0ux17e7.execute-api.us-east-1.amazonaws.com'],
                                  'Postman-Token': ['b30be14f-d1ce-47fe-b68d-0a272200cac5'],
                                  'User-Agent': ['PostmanRuntime/7.31.0'],
                                  'Via': ['1.1 95edb2a6efdb5ee4d3c7f7aa298bb2f2.cloudfront.net (CloudFront)'],
                                  'X-Amz-Cf-Id': ['Du8C80Yb59Mbb-ReCPO2i2qmZm6epLm87ZK4yf_ytUlwFeFAJzg6Dw=='],
                                  'X-Amzn-Trace-Id': ['Root=1-63f3f66c-453eb11b265c5ea13e8523f4'],
                                  'X-Forwarded-For': ['98.216.16.152, 130.176.166.15'], 'X-Forwarded-Port': ['443'],
                                  'X-Forwarded-Proto': ['https']}, 'queryStringParameters': None,
            'multiValueQueryStringParameters': None, 'pathParameters': None, 'stageVariables': None,
            'requestContext': {'resourceId': 'pukd69', 'resourcePath': '/event', 'httpMethod': 'POST',
                               'extendedRequestId': 'AqNw_Gb9oAMFa8w=', 'requestTime': '20/Feb/2023:22:38:36 +0000',
                               'path': '/Prod/event', 'accountId': '208827447334', 'protocol': 'HTTP/1.1',
                               'stage': 'Prod', 'domainPrefix': 'acm0ux17e7', 'requestTimeEpoch': 1676932716498,
                               'requestId': '8d0c3cb3-914e-409e-8262-f3b5feeb83ed',
                               'identity': {'cognitoIdentityPoolId': None, 'accountId': None, 'cognitoIdentityId': None,
                                            'caller': None, 'sourceIp': '98.216.16.152', 'principalOrgId': None,
                                            'accessKey': None, 'cognitoAuthenticationType': None,
                                            'cognitoAuthenticationProvider': None, 'userArn': None,
                                            'userAgent': 'PostmanRuntime/7.31.0', 'user': None},
                               'domainName': 'acm0ux17e7.execute-api.us-east-1.amazonaws.com', 'apiId': 'acm0ux17e7'},
            'body': '{ "body":{\r\n    "eventType": "getEvent",\r\n    "eventId": "123456",\r\n    "mode": "test"\r\n}\r\n}',
            'isBase64Encoded': False}
