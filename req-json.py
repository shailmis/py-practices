'''
 Use rest api to get a JSON and traverse it (REST API calling using recursion), 
 recursive requests to Directory API (url), Recursive call of LinkedIn api using REST.  
 Calling rest api and parsing data.
'''

import requests

payload = {'page': 10, 'count': 25}
r = requests.get("https://httpbin.org/get",params=payload)

print(r.status_code)
#print(r.text)
print(r.url)
#print(r.json())

r_dict = r.json()

for (k,v) in r_dict.items():
    print(k)
print(type(r_dict))


r_auth = requests.get("https://httpbin.org/basic-auth/shailem/testing",auth=('shailem','testing'))
print(r_auth.text)