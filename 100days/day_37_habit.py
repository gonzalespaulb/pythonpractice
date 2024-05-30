import requests
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv("/Users/paulgonzales/Desktop/pythonpractice/100days/stock.env")

print(os.getenv("PIXELA_TOKEN"))

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": os.getenv("PIXELA_TOKEN"), 
    "username": "paulie", 
    "agreeTermsOfService": "yes", 
    "notMinor": "yes"

}

response = requests.post(url=pixela_endpoint, json=user_params)
print(response.text)