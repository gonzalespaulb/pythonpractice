import requests
import datetime as dt

# from twilio.rest import Client

# account_sid = 'AC98e0ded99bf88cf08ab4da2977bda8da'
# auth_token = '1b1d8dc0b5f34d8deabb7c82841b36b5'
# client = Client(account_sid, auth_token)

# message = client.messages.create(
#   from_='+18448110673',
#   body='Hello from Twilio',
#   to='+18777804236'
# )

# print(message.status)

import smtplib

my_email = "paulgonzales.subscriptions@gmail.com"
to_email = "gonzalespaulb@gmail.com"
my_password = "wkvn cwzd mrla bbdr"

def send_email(time): 
    with smtplib.SMTP("smtp.gmail.com") as connection: 
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs=to_email, msg=f"Subject: Rain Alert!\n\nwill start raining at {time}.")


key = "88ffe76f46b1a0705522c3c415b3c8f1"
lat = 39.396969
lon = -107.217529
cnt = 4
api = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={key}&cnt={cnt}"
api = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={key}"
data = requests.get(api).json()

# Weather code less than 700 = umbrella

# cod
# message
# cnt
# list
# city

# dt
# main
# weather
# clouds
# wind
# visibility
# pop
# sys
# dt_txt


weather_list = data["list"]

for key in weather_list:
    timestamp = key["dt"]
    will_rain = False
    formatted_timestamp = dt.datetime.fromtimestamp(timestamp)
    
    weather_list = key["weather"]
    for weather in weather_list: 
        condition_code = weather["id"]
        will_rain = True if condition_code < 700 else False

    # send_email(formatted_timestamp) if will_rain else None
    