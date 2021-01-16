"""Pixela Habit Tracker Main Module"""
import os
import datetime as dt
import requests

# Environmental variables - pixela token and username, they are arbitrary token and username.
# replace the os.environ.get values by your own token and username
# token example - sdasd12kjn3
# name example -"john" - all in small letters

pixela_token = os.environ.get("token")
pixela_username = os.environ.get("username")

# Graph data
GRAPH_ID = "graph1"
GRAPH_NAME = "coding"
GRAPH_UNIT = "Hour"
GRAPH_UNIT_TYPE = "float"
GRAPH_COLOR = "ajisai"

# Posting a value to the today
# DATE = str(dt.datetime.now().strftime("%Y%m%d"))
# uncomment the line below for a custom date
DATE = str(dt.datetime(year=2021, month=1, day=14).strftime("%Y%m%d"))

# Today's value- No of graph units in string format for the date, 3 is an example
QUANTITY_TODAY = "3"

# Pixela endpoint
PIXELA_ENDPOINT = "https://pixe.la/v1/users"

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
    "date": DATE,
    "quantity": QUANTITY_TODAY,
}

# Add value to the graph
add_value_response = requests.post(url=graph_url, headers=headers, json=value_config)
