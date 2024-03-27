import requests

d = {"name":"morpheus","job":"leader"}

x=requests.post(url="https://reqres.in/api/users",json=d)
print(x.json)