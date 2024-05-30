import requests
import datetime as dt
from dotenv import load_dotenv
import os
load_dotenv()
import smtplib

my_email = "paulgonzales.subscriptions@gmail.com"
to_email = "gonzalespaulb@gmail.com"
my_password = "wkvn cwzd mrla bbdr"

def send_email(time): 
    with smtplib.SMTP("smtp.gmail.com") as connection: 
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs=to_email, msg=f"Subject: Rain Alert!\n\nwill start raining at {time}.")



key = os.getenv("ISS_KEY")
lat = 39.396969
lon = -107.217529
cnt = 4
api = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={key}&cnt={cnt}"
api = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={key}"
data = requests.get(api).json()


weather_list = data["list"]

for key in weather_list:
    timestamp = key["dt"]
    will_rain = False
    formatted_timestamp = dt.datetime.fromtimestamp(timestamp)
    
    weather_list = key["weather"]
    for weather in weather_list: 
        condition_code = weather["id"]
        will_rain = True if condition_code < 700 else False

    