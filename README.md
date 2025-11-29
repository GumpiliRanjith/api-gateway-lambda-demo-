# api-gateway-lambda-demo-
# API Gateway + AWS Lambda (Query Parameter Demo)

This project demonstrates how to build a simple serverless API using Amazon API Gateway integrated with an AWS Lambda function. The API accepts a query parameter (`name`) and responds with a personalized message.

## Features
- GET endpoint using API Gateway
- Lambda integration (Python)
- Handles query parameters


- Returns JSON responses
- Basic error handling

## Lambda Function
The Lambda function reads a `name` parameter from the query string.  
If the parameter is missing, it returns a 400 error.

### Example Request
{
“message”: “Hello Topper, your request is processed!”
}
## How to Test the API

### 1. Test in Lambda Console
Use this test event:
