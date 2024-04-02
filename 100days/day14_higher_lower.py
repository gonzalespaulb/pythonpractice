# Higher or lower game

# Create a dictionary with the key and value

# Create random matchups 

# Have a loop with an input for which one is higher or lower

import random

country_sizes = {
    "Russia": 17098242, 
    "Canada": 9984670,
    "China": 9706961, 
    "USA": 9372610, 
    "Brazil": 8515767,
    "Australia": 7692024,
    "India": 3287590,
    "Argentina": 2780400, 
    "Kazakhstan": 2724900, 
    "Algeria":2381741,
}

country_keys = []

for countries in country_sizes: 
    country_keys.append(countries)

score = 0
lives = 5

while True: 

    country_1 = country_keys[random.randint(0, len(country_keys) - 1)]
    country_2 = country_keys[random.randint(0, len(country_keys) - 1)]

    if country_1 == country_2: 
        continue

    correct_country = (country_1 if country_sizes[country_1] > country_sizes[country_2] else country_2).lower()

    which_country = input(f"Which country has a bigger landmass? {country_1} or {country_2}\n").lower()

    if which_country == correct_country: 
        score += 1
        print("That's correct!")
        continue

    elif which_country != correct_country and lives > 0: 
        lives -= 1
        print("Wrong answer")
        continue

    else: 
        print(f"Total score is {score}")
        break