import uuid
import json


def hello(event, context):
    return {
        "headers": {
            "Content-Type": "text/plan"
        },
        "statusCode": 200,
        "body": "olá python " + str(uuid.uuid4()),
    }
