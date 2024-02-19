import time
import os

"""
This is a comment
"""

currTime = time.localtime()

currentDate = str(currTime.tm_mon) + "/" + str(currTime.tm_mday) + "/" + str(currTime.tm_year)

# print(currentDate)

desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

folder_name = input("What shall we call this folder? ")

new_folder_path = os.path.join(desktop_path, folder_name)

# os.makedirs(new_folder_path)