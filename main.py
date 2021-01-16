"""Pixela Habit Tracker Main Module"""
import os
import requests
import datetime as dt
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

# Today's value- No of graph units in string format
QUANTITY_TODAY = "3"

# Posting a value to the today
date = str(dt.datetime.now().strftime("%Y%m%d"))
# uncomment the line below for a custom date
# date = str(dt.datetime(year=2021, month=1, day=15).strftime("%Y%m%d"))
print(date)
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

# To view your graph url in the browser or update a value in it
graph_url = f"{GRAPH_ENDPOINT}/{GRAPH_ID}"

# Graph value configuration
value_config = {
    "date": date,
    "quantity": QUANTITY_TODAY,
}

# Add value to the graph
add_value_response = requests.post(url=graph_url, headers=headers, json=value_config)
print(add_value_response.text)
