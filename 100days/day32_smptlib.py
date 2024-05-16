import smtplib

my_email = "paulgonzales.subscriptions@gmail.com"
to_email = "gonzalespaulb@gmail.com"
my_password = "wkvn cwzd mrla bbdr"

# connection = smtplib.SMTP("smtp.gmail.com", 587)
# connection.starttls()
# connection.login(user=my_email, password=my_password)
# connection.sendmail(from_addr=my_email, to_addrs=to_email, msg="Subject: Testing, test, test\n\nThis is the body of my email")
# connection.close()

# NOTE ----- ------------- SO NO NEED TO CLOSE

def send_email(name:str, age:int): 
    with smtplib.SMTP("smtp.gmail.com") as connection: 
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs=to_email, msg=f"Subject: {name}'s Birthday Today!\n\n{age} years young today.")


# NOTE ------------------- RUN THIS AUTOMATICALLY IN PYTHONANYWHERE

import datetime as dt
import pandas as pd

birthday_file = "./100days/birthdays.csv"

date_of_birth = dt.datetime(year=1996, month=6, day=23)

data = pd.read_csv(birthday_file)

birthdays_dict = {str(row["Name"]):str(row["Birthday"]) for _, row in data.iterrows()}

for person in birthdays_dict:

    birthday = birthdays_dict[person]
    month = int(birthday.split("-")[0])
    day = int(birthday.split("-")[1])
    year = int(birthday.split("-")[2])

    now = dt.datetime.now()
    formatted_birthday = dt.datetime(month=month, day=day, year=year)

    if now.month == formatted_birthday.month and now.day == formatted_birthday.day: 
        age = now.year - formatted_birthday.year
        send_email(person, age)