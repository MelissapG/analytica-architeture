from flask.globals import request
import requests

BASE = "http://127.0.0.1:5000/"

data = [{"likes":1, "name": "Melissa", "views":10}, 
        {"likes":2, "name": "Mel", "views":20},
        {"likes":3, "name": "Mi", "views":30}]

for i in range(len(data)):
    response = requests.put(BASE+"video/" +str(i), data[i])
    print(response.json())
input()

response = requests.get(BASE+"video/0")
print(response.json())
input()

response = requests.patch(BASE+"video/0", {"views":101})
print(response.json())

input()
response = requests.get(BASE+"video/0")
print(response.json())