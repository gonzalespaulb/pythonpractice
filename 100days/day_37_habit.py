import requests
from dotenv import load_dotenv
import os
import datetime as dt


load_dotenv("/Users/paulgonzales/Desktop/pythonpractice/100days/stock.env")

USERNAME = "paulie"
TOKEN = os.getenv("PIXELA_TOKEN")
TODAY = dt.datetime.now()

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN, 
    "username": USERNAME, 
    "agreeTermsOfService": "yes", 
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": "italian", 
    "name": "Italian Graph", 
    "unit": "min", 
    "type": "float", 
    "color": "ajisai"
}

HEADERS = {"X-USER-TOKEN": TOKEN}

body = {
    "date": TODAY.strftime("%Y%m%d"), 
    # "date": TODAY.strftime("20240601"), 
    "quantity": "0", 
}

session_on = True

while session_on: 

    which_date = input("Which date would you like to update? t = today q = quit or yyyymmdd\n").lower()

    if which_date == "t": 
        body["date"] = TODAY.strftime("%Y%m%d")
        body["quantity"] = input("What is the quantity?\n")

    elif which_date == "q": 
        session_on = False

    else: 
        body["date"] = which_date
        body["quantity"] = input("What is the quantity?\n")
    
    create_pixel = requests.post(url=f"{pixela_endpoint}/{USERNAME}/graphs/{graph_config['id']}", headers=HEADERS, json=body)
    print(create_pixel.text)

    add_another = input("Add another pixel? y or n\n")

    if add_another == "y": 
        continue

    else: 
        session_on = False


# response = requests.post(url=graph_endpoint, json=graph_config, headers=HEADERS)   
# update_pixel = requests.put(url=f"{pixela_endpoint}/{USERNAME}/graphs/{graph_config['id']}/{body['date']}", headers=HEADERS, json=body)
# delete_pixel = requests.delete(url=f"{pixela_endpoint}/{USERNAME}/graphs/{graph_config['id']}/{body['date']}", headers=HEADERS)
# create_pixel = requests.post(url=f"{pixela_endpoint}/{USERNAME}/graphs/{graph_config['id']}", headers=HEADERS, json=body)