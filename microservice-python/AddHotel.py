import json
import boto3
import logging
import multipart
import base64

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def handler(event, context):

    headers = {
        "Access-Control-Allow-Headers": "*",
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "*"
    }
    
    body = event["body"]
    isBase64Encoded = bool(event["isBase64Encoded"])
    
    # decode if body in base64
    if isBase64Encoded:
        body = base64.b64decode(body)
    else:
        body = body.encode('utf-8')
        
    parser = multipart.FormDataParser(body)
    parts = parser.parse()
    
    hotel_name = parts.get('hotelName')
    hotel_rating = parts.get('hotelRating')
    hotel_city = parts.get('hotelCity')
    hotel_price = parts.get('hotelPrice')
    file_name = parts.get('fileName')
    user_id = parts.get('userId')
    id_token = parts.get('idToken')
    
    file = parts.get('filedata').file.read()
    
    logger.info("This is some information right here")
    
    return {
        'statusCode': 200,
        'headers': headers,
        'body': json.dumps(event['key1'])
    }
