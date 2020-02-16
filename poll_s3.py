from flask import Flask, json, request
api = Flask(__name__)

@api.route('/poll', methods=['GET'])
def get_pages():
  return json.dumps({'Success':'S3 pages'})

@api.route('/poll', methods=['POST'])
def post_pages():
  print(request.form)
  return json.dumps({'Success':request.form})

if __name__ == '__main__':
  api.run(host='0.0.0.0', port=80)