import requests
import json
import pandas as pd

url="http://127.0.0.1:5000/books"

headers={
    'Content-type':'application/json'
}

response=requests.get(url,headers=headers)
received_data=response.json()
print(response.content,type(response.content))

send_data={
        'Game of thrones':{
            'Author':'RR Martin',
            'release_year':'1994',}
            }

response=requests.put('http://127.0.0.1:5000/book/GOT',headers=headers,json=send_data)
print(response.status_code)

response=requests.get(url,headers=headers)
received_data=response.json()
print(received_data)

with open('book.json','w') as file:
    json.dump(received_data,file)

with open('book.json','r') as file:
    read_data=json.load(file)
    print(read_data)



