import requests
import os

# Environmental variables - pixela token and username, they are arbitrary token and username.
pixela_token = os.environ.get("token")
pixela_username = os.environ.get("username")
pixela_endpoint = "https://pixe.la/v1/users"

