import uuid
import json
import requests


def hello(event, context):
    res = requests.get('https://scotch.io')
    return {
        "headers": {
            "Content-Type": "application/json"
        },
        "statusCode": res.status_code,
        "body": json.dumps({
            "message": "olá python " + str(uuid.uuid4())
        }),
    }
