# Event Service API

## Endpoint

The API endpoint is `/event`. 

## Request Format

### GET `/event`

This API retrieves information for a specific event.

**Request Parameters:**

| Parameter  | Required | Type   | Description         |
| ---------- | -------- | ------ | ------------------- |
| eventId    | Yes      | string | ID of the event to retrieve |

**Request Example:**

```json
{
    "eventType": "getEvent",
    "eventId": "123456"
}

```

**Response Format:**

```json
{
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
