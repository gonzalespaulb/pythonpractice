# numbers = [1, 2, 3]
# new_numbers = [n + 1 for n in numbers]

names = ["Paul", "Martha", "Mike", "Will"]

# Return only names 4 and less letters
short_names = [name for name in names if len(name) < 5]

# Upper case all the names
upper_case_names = [name.upper() for name in names]

# Square each number
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

squared_numbers = [number * number for number in numbers]
# print(squared_numbers)

even_numbers = [number for number in numbers if number % 2 == 0]
# print(even_numbers)

# Text file exercise ----------------------------------- overlapping data

text_file_1 = "./100days/day_26_1.txt"
text_file_2 = "./100days/day_26_2.txt"

with open(text_file_1, mode="r") as file:
    data = file.readlines()
    file_1 = []

    for item in data: 
        if not item == '\n': 
            stripped_item = item.rstrip("\n")
            file_1.append(stripped_item)

with open(text_file_2, mode="r") as file:
    data = file.readlines()
    file_2 = []

    for item in data: 
        if not item == '\n': 
            stripped_item = item.rstrip("\n")
            file_2.append(stripped_item)

overlapping_data = [num for num in file_1 if num in file_2]
# print(overlapping_data) 

# Dictionary ----------------------------------- Dictionary

import random

student_scores = {name:random.randint(60, 100) for name in names}
# print(student_scores)

passed_students = {name:student_scores[name] for name in student_scores if student_scores[name] > 70}
# print(passed_students)

# Create a dictionary from the sentence ----------------------------------- Create a dictionary from the sentence

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
number_of_letters = {word:len(word) for word in sentence.split(" ")}
# print(number_of_letters)

# Nato Project ----------------------------------- Nato Project
# User iterrows


# 1. Turn CSV into a dictionary - - - - {A: Alpha, B: Bravo}
# 2. Create a list of phonetic code words from a word
# 3. Input a word shit out a list of phonetics

nato_file = "./100days/nato_alphabet.csv"

import pandas as pd

data = pd.read_csv(nato_file)

sample_word = "Paul"

nato_dict = {str(row["letter"]):str(row["code"]) for _, row in data.iterrows()}

natoed_word = [nato_dict[letter] for letter in sample_word.upper()]

print(natoed_word)
