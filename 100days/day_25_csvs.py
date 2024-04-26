weather_file = "./100days/weather_data.csv"
squirrel_file = "./100days/squirrel_data.csv"
# employee_file = "./100days/employee_data.csv"

# with open(weather_file, mode="r") as file: 
#     data = file.readlines()

# print(data)

# import csv

# with open(weather_file) as file: 
#     data = csv.reader(file)
#     temperatures = []

#     for row in data: 
#         if row[1].isdigit(): 
#             temperatures.append(int(row[1]))

#     print(temperatures)

# ------------------------------------------------- TEMPERATURE CSV -------------------------------------------------#

import pandas

data = pandas.read_csv(weather_file)
# print(type(data))
# print(data["temp"].to_list())

temp_list = data["temp"].to_list()

avg_temp = sum(temp_list) / len(temp_list)

# print(f"The average temperature this week is {avg_temp} Fahrenheit")

# How to print a row
# print(data[data["day"] == "Monday"])

# Finding the hottest row
hottest_temp = data["temp"].max()
hottest_row = data[data["temp"] == hottest_temp]

# print(hottest_row["condition"])



# employee_data = pandas.read_csv(employee_file)
pandas.set_option('display.max_rows', None)
# find_paul = employee_data[employee_data["firstName"] == "Paul"]
# print(find_paul["email"])

# print(employee_data)



# ------------------------------------------------- SQUIRREL DATA -------------------------------------------------#
# 
# 

fur_colors = []
squirrels = pandas.read_csv(squirrel_file)
fur_color_data = squirrels["Primary Fur Color"].to_list()
fur_color_dict = {}

# Compile all colors
for color in fur_color_data: 
    if not color in fur_colors: 
        fur_colors.append(color)

# Create dictionary for color count
for color in fur_colors: 
    fur_color_dict[color] = 0

# Tally for every color
for color in fur_color_data: 
    if color in fur_color_dict: 
        fur_color_dict[color] += 1

new_frame = {
    "Fur Color": [],
    "Count": []
}

# Reformat dict for data frame
for key in fur_color_dict: 
    new_frame["Fur Color"].append(key)
    new_frame["Count"].append(fur_color_dict[key])


squirrel_count = pandas.DataFrame(new_frame)
print(squirrel_count)