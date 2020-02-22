from flask import Flask, json, request
import boto3
from hashlib import sha256
api = Flask(__name__)

@api.route('/poll', methods=['GET'])
def get_pages():
  return json.dumps({'Success':'S3 pages'})

@api.route('/poll', methods=['POST'])
def post_pages():
    
    session = boto3.Session(profile_name='default')
    s3 = session.resource('s3')
    body = request.get_data()
    body = json.loads(body)
    body = body['Message']
    records = json.loads(body)
    key = records['Records'][0]['s3']['object']['key']
    if key.endswith('/hash'):
        return json.dumps({'Success':request.form})

    contents = s3.Object('storage-web',key)
    contents = contents.get()['Body'].read().decode('utf-8')
    hashedWord = sha256(contents.encode('utf-8')).hexdigest()
    print(hashedWord)
    object = s3.Object('storage-web', key+'/hash')
    object.put(Body=hashedWord)
  
    return json.dumps({'Success':request.form})

if __name__ == '__main__':
  api.run(host='0.0.0.0', port=80)
