"""Pixela Habit Tracker Main Module"""
import os
from datetime import datetime
import requests

# ---------------------------- TOKEN, USERNAME AND API ENDPOINT  ------------------------------- #
# Environmental variables - pixela token and username, they are arbitrary token and username.
# replace the os.environ.get values by your own token and username
# token example - sdasd12kjn3
# name example -"john" - all in small letters
token = os.environ.get("token")
user_name = os.environ.get("username")

# Pixela endpoint
PIXELA_ENDPOINT = "https://pixe.la/v1/users"

# API request header
headers = {
    "X-USER-TOKEN": token
}


# ---------------------------- NEW USER ------------------------------- #
# Creating a new USER
def create_user():
    """Function to create user- run only once"""
    user_params = {
        "token": token,
        "username": user_name,
        "agreeTermsOfService": "yes",
        "notMinor": "yes",
    }
    create_user_response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
    print(create_user_response.text)


# ---------------------------- NEW GRAPH ------------------------------- #
# Creating a new GRAPH
# Graph data
GRAPH_ID = "graph1"
GRAPH_NAME = "coding"
GRAPH_UNIT = "Hour"
GRAPH_UNIT_TYPE = "float"
GRAPH_COLOR = "ajisai"

# Creating graph
GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{user_name}/graphs"


# Graph request header


def create_graph():
    """Function to create new graph - run only once for one graph"""
    graph_config = {
        "id": GRAPH_ID,
        "name": GRAPH_NAME,
        "unit": GRAPH_UNIT,
        "type": GRAPH_UNIT_TYPE,
        "color": GRAPH_COLOR
    }

    # Creating a graph- a one time request
    graph_response = requests.post(url=GRAPH_ENDPOINT, json=graph_config, headers=headers)
    print(graph_response.text)


# ---------------------------- NEW VALUE ------------------------------- #
graph_url = f"{GRAPH_ENDPOINT}/{GRAPH_ID}"


def create_new_value(date, qty):
    """Function to create new value"""
    # Graph value configuration
    value_config = {
        "date": date,
        "quantity": qty,
    }

    # Add value to the graph
    add_value_response = requests.post(url=graph_url, headers=headers, json=value_config)
    print(add_value_response.text)


# ---------------------------- DELETE VALUE ------------------------------- #
# Deleting value function
def delete_value(date):
    """function to delete a pixel/value from the graph"""
    endpoint = f"{graph_url}/{date}"
    delete_response = requests.delete(url=endpoint, headers=headers)
    print(delete_response.text)


# ---------------------------- UPDATE VALUE ------------------------------- #
# Deleting value function
def update_value(date, qty):
    """function to update a pixel/value from the graph"""

    # new pixel/value date
    new_pixel_data = {
        "quantity": qty
    }
    endpoint = f"{graph_url}/{date}"
    put_response = requests.put(url=endpoint, headers=headers, json=new_pixel_data)
    print(put_response.text)


# ---------------------------- RUNNING THE PROGRAM  ------------------------------- #
# UNCOMMENT AFTER RUNNING ONCE, AFTER CREATING NEW USER AND GRAPH
# Creating a new user
create_user()

# Creating a new graph
create_graph()


# ---------------------------- CREATING A DATE  ------------------------------- #
# Today
DATE = datetime.now()
# OR A CUSTOM DATE - UNCOMMENT IF NOT NEEDED
DATE = datetime(year=2021, month=1, day=16)

# Formatting date
DATE = str(DATE.strftime("%Y%m%d"))

# ---------------------------- CREATE/UPDATE/DELETE VALUE  ------------------------------- #
# Uncomment unwanted functions
# Quantity of graph units/value/pixels in string FOR NEW VALUE OR UPDATING VALUE
QUANTITY = "7"

# Creating new value
create_new_value(date=DATE, qty=QUANTITY)

# Updating value
update_value(date=DATE, qty=QUANTITY)

# Deleting value
delete_value(date=DATE)

# PRINT URL FOR ACCESSING IN BROWSER
BROWSER_URL = f"{graph_url}.html"
print(BROWSER_URL)
