import json
import boto3
import logging
import multipart
import base64
import jwt

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
    
    token = jwt.decode(id_token, verify=False)
    group = token.get("cognito:groups")
    
    if group is None or group != "Admin":
        return {
            "statusCode" : 401,
            "body" : json.dumps({
                "Error" : "Sorry, you are not a member of admin group"
            })
        }
        
    bucket_name = os.environ.get("bucketName")
    region = os.environ.get("AWS_REGION")
    
    s3_client = boto3.client("s3", region_name = region)
    
    try:
        s3_client.put_object(
            Bucket = bucket_name,
            Key = file_name,
            Body = file
        )
    except Exception as e:
        return {
            "statusCode" : 500,
            "body" : json.dumps({
                "Error" : "Oh no, uploading the hotel photo failed"
            })
        }
        
    
    logger.info("This is some information right here")
    
    return {
        'statusCode': 200,
        'headers': headers,
        'body': json.dumps(event['key1'])
    }
