import json
import urllib.request
import boto3
import botocore

bucket = 'storage-web'

def lambda_handler(event, context):
        
    url = event['url']
    url = url.replace("'", "")
    if not url.startswith('http'):
        url = 'http://' + url
    open_url = urllib.request.urlopen(url).read()
    pos = url.find('//')
    key = url[pos+2:].replace("/", ".")
    
    s3 = boto3.resource('s3')
    
    object = s3.Object(bucket, key)
    object.put(Body=str(open_url))

    try:
        s3.Object(bucket, key).load()
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == '404':
            return {
                'statusCode': 404,
                'body': 'Failed!'
            }
        else:
            return {
                'statusCode': 500,
                'body': 'Failed!'
            }
    else:
        message = 'Page with url ', url, ' stored successfully'
        return {
            'statusCode': 200,
            'body': message
        }