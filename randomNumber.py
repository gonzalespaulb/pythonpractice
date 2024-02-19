import random

top_of_range = input("Type a number ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please type a number larger than zero")
        quit()

else:
    print("Type in a digit please")
    quit()


random_number = random.randint(0, top_of_range)

guesses = 0

while True: 

    user_guess = input("Make a guess ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please enter a number next time")
        continue

    if user_guess == random_number: 
        print("You got it")
        guesses += 1
        break
    else: 
        if(user_guess > random_number):
            print("You guessed too high")
        else:
            print("You guessed too low")
        guesses += 1

print("You got it in", guesses, "guesses")
    

