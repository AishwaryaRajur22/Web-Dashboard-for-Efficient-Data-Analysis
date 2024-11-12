import requests
import json
import pandas as pd

# Importing Libraries:
# requests: Used for making HTTP requests to interact with APIs.
# json: Used for handling JSON data.
# pandas: Used for data manipulation and exporting data to an Excel sheet.

url = "http://127.0.0.1:5000/books"

# This header specifies that the content type of the request is JSON.

headers = {
  'Content-Type': 'application/json'
}

# requests.get(): Sends a GET request to the API endpoint to retrieve data.
# response.json(): Converts the response content from a JSON string into a Python dictionary.

#GET
response=requests.get(url,headers=headers)
data=response.json()

print(response.content, type(response.content))
# response.content is by default a encoded string and response.json() converts response.content to dictionary. 
print(data)

# requests.put(): Sends a PUT request to update or create the resource at the specified endpoint (/book/GOT).
# json=send_data: Converts the send_data dictionary into a JSON string for the request body.

#PUT
send_data = { "book name":"Game of Thrones"}

response=requests.put("http://127.0.0.1:5000/book/GOT", headers=headers, json=send_data)
#json=send_data will convert dict to string while sending, also change endpoint in the url
print(response.status_code)


#POST

response=requests.post("http://127.0.0.1:5000/book/GOT",headers=headers,json=send_data)
print(response.status_code)
#just to check status code

#DELETE

# requests.delete(): Sends a DELETE request to remove the resource at the specified endpoint.
response=requests.delete("http://127.0.0.1:5000/book/GOT")
print(response.status_code)

#to check if GOT got deleted 
response=requests.get(url,headers=headers)
data=response.json()
print(response.content, type(response.content))
# response.content is by default a encoded string and response.json() converts response.content to dictionary. 
print(data)


data["Eragon"]["release_year"] = 2004

response=requests.put("http://127.0.0.1:5000/book/Eragon", headers=headers, json=data["Eragon"])
#json=send_data will convert dict to string while sending, also change endpoint in the url
print(response.status_code)

#to check if GOT got deleted 
response=requests.get(url,headers=headers)
data=response.json()
print(response.content, type(response.content))
# response.content is by default a encoded string and response.json() converts response.content to dictionary. 
print(data)

#for excel

df = pd.DataFrame.from_dict(data)
df.to_excel("updated_books.xlsx")


#to write
with open("all books.json",'w') as file:
    json.dump(data,file)

#to read
with open("all books.json",'r') as file:
    read_data = json.load(file)
    print(read_data)

#to read it as string
with open("all books.json",'r') as file:
    x = file.read()
    print(x, type(x))














exit()


















import json
import requests

response = requests.request("GET", "http://127.0.0.1:5000/books")
fetched_data = response.json()
with open("all_books.json", "w") as f:
    json.dump(fetched_data, f)
print(response.json(), response.status_code)

response = requests.request("GET", "http://127.0.0.1:5000/book/Eragon")
fetched_data = response.json()
with open("eragon.json", "w") as f:
    json.dump(fetched_data, f)
print(response.json(), response.status_code)

# payload = {"Author": "Rowling"}
# headers = {
#   'Content-Type': 'application/json'
# }
# response = requests.request("PUT", "http://127.0.0.1:5000/book/HarryPotter", headers=headers, data = json.dumps(payload))
# print(response.json(), response.status_code)

# response = requests.request("DELETE", "http://127.0.0.1:5000/book/HarryPotter")
# print(response.status_code)

# response = requests.request("GET", "http://127.0.0.1:5000/books")
# print(response.json(), response.status_code)
