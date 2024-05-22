import requests
import datetime as dt

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

    print(formatted_timestamp, "Bring Umbrella" if will_rain else "")
    