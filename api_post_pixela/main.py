from time import strftime

import requests
import datetime as dt
TOKEN = "gierijmewkeljf"
USERNAME = "test"
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
GRAPH_ID = "graph1"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
#create user

response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
print(response.text)

headers = {
    "X-USER-TOKEN": TOKEN
}
graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"


graph_params = {
    "id":GRAPH_ID,
    "name":"Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

requests.post(url=graph_endpoint,json=graph_params, headers=headers)

pixela_creation_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"

today = dt.datetime.now()
pixela_data ={
    "date": today.strftime("%Y%m%d"),
    "quantity": "10.0"
}

requests.post(url=pixela_creation_endpoint, headers=headers, json=pixela_data)