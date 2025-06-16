import requests
import json

base_url = "https://swapi.info/api/"
endpoint = "people/5/"
# Response object
response = requests.get(base_url + endpoint)
# print("Response Type: \n",response)
# print("Response Text: \n",response.text)
# print("Status Code: \n",response.status_code)
# print("Headers: \n",response.headers)
data = response.json()
print(data['name'])