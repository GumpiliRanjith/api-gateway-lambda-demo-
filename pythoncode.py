import json

def lambda_handler(event, context):
    params = event.get("queryStringParameters") or {}
    name = params.get("name")

    if not name:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "Missing 'name' query parameter"})
        }

    greeting = f"Hello {name}, your request is processed!"

    return {
        "statusCode": 200,
        "body": json.dumps({"message": greeting})
    }