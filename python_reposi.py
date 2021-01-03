import requests
url = 'https://api.github.com/search/repositories?q=language:python&sort=start'
headers = {'Accept':'application/vnd.github.v3+json'}
r = requests.get(url,headers = headers)
print('Status code : {}'.format(r.status_code))
response_dict = r.json()
print(response_dict.keys())