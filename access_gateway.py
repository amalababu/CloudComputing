import requests

# url = 'http://courses.cse.tamu.edu/chiache/csce678/s20/projects.html'
url = input("Please enter url")
response = requests.get('https://ioqe1193xa.execute-api.us-west-2.amazonaws.com/default/pageStore', params={'url': url},)

if response.status_code == 200:
    print('Success!')

elif response.status_code == 404:
    print('Not Found.')