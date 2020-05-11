import uuid
import json
import requests


def hello(event, context):
    res = requests.get('https://scotch.io')
    return {
        "headers": {
            "Content-Type": "text/plan"
        },
        "statusCode": res.status_code,
        "body": "olá python " + str(uuid.uuid4()),
    }
