import requests

url = "http://172.16.131.14:3030/da/query"

payload = "query=SELECT%20%3Fsubject%20%3Fpredicate%20%3Fobject%0AWHERE%20%7B%0A%20%20%3Fsubject%20%3Fpredicate%20%3Fobject%0A%7D%0ALIMIT%2025"
headers = {
    'Content-Type': "application/x-www-form-urlencoded",
    'cache-control': "no-cache",
    'Postman-Token': "681d8312-7fab-40ab-b91d-e1926ad703cd"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)