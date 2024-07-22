import json


def hello(event, context):
    body = {
        "message": "Go Serverless v3.0! Your function executed successfully through CircleCI!",
        "input": event,
    }

    return {"statusCode": 200, "body": json.dumps(body)}
