import json
import boto3
import base64
from urllib import parse


def lambda_handler(event, context):
    try:
        # TODO implement
        s3 = boto3.client('s3')
        # message = {"first_name":event["first_name"], "last_name":event["last_name"]}
        bucket_name = 'inspection-images-bucket'
        file_name_with_extension = 'myjpeg7.jpg'
        data = json.loads(event['body'])
        name = data['name']
        image = data['file']
        image = image[image.find(",") + 1:]
        dec = base64.b64decode(image + "===")
        s3.put_object(Bucket=bucket_name, Key=name, Body=dec)

        # obj = s3.Object(bucket_name,file_name_with_extention)
        # obj.put(Body=base64.b64decode(image_base64))
        response_object = {
            'statusCode': 200,
            'body': "hello"
        }
    except Exception as e:
        response_object = {
            'statusCode': 200,
            'body': str(e)
        }
    return response_object