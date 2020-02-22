import requests
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("url", help="Enter url of webpage to be stored")
args = parser.parse_args()

url = args.url # input("Please enter url")
response = requests.get('https://ioqe1193xa.execute-api.us-west-2.amazonaws.com/default/pageStore', params={'url': url},)

if response.status_code == 200:
    print('Success!')

elif response.status_code == 404:
    print('Not Found.')