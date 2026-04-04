import requests
import datetime
import os

USERNAME = os.environ.get("USERNAME")
TOKEN = os.environ.get("TOKEN")

print(USERNAME, TOKEN)
pixela_url = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_url, json=user_params)
# print(response.text)

graph_url = f"{pixela_url}/{USERNAME}/graphs"

graph_params = {
    "id": "graph1",
    "name": "Circuit Graph",
    "unit": "hours",
    "type": "float",
    "color": "momiji"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_url, json=graph_params, headers=headers)
# print(response.text)

today = datetime.datetime.now()
print(today)

pixel_url = f"{graph_url}/graph1"



pixel_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "0.5",
}

response = requests.post(url=pixel_url, json=pixel_params, headers=headers)
print(response.text)