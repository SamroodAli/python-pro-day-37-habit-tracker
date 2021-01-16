"""Pixela Habit Tracker Main Module"""
import os
import requests

# Environmental variables - pixela token and username, they are arbitrary token and username.
pixela_token = os.environ.get("token")
pixela_username = os.environ.get("username")
PIXELA_ENDPOINT = "https://pixe.la/v1/users"

# Graph data
GRAPH_ID = "graph1"
GRAPH_NAME = "coding"
GRAPH_UNIT = "Hour"
GRAPH_UNIT_TYPE = "float"
GRAPH_COLOR = "ajisai"


user_params ={
    "token": pixela_token,
    "username": pixela_username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
response = requests.post(url=PIXELA_ENDPOINT, json=user_params)

# Graph data
GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{pixela_username}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": GRAPH_NAME,
    "unit": GRAPH_UNIT,
    "type": GRAPH_UNIT_TYPE,
    "color": GRAPH_COLOR
}
# Graph request header
headers ={
    "X-USER-TOKEN": pixela_token
}
# Creating a graph- a one time request
graph_response = requests.post(url=GRAPH_ENDPOINT, json=graph_config, headers=headers)

# To view your graph url in the browser - requesting html
graph_url = f"{GRAPH_ENDPOINT}/{GRAPH_ID}.html"
print(f"Here is your graph link:\n{graph_url}")
