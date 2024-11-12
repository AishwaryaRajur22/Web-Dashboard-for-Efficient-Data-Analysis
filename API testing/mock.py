import requests


url='https://api.apis.guru/v2/list.json'
response=requests.get(url)
data=response.json()
print(data)

