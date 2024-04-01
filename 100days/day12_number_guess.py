# Does user want to play hard or easy.

# Number of guesses

# Loop to check if number is too high or too low

# Every loop subtract a guess

# If guesses does not equal zero and guess is equal to actual number end game you win

# IF guesses equal to 0 you lose

import random

number_to_guess = random.randint(1, 100)

play_mode = input("What play mode would you like to do? hard or easy.\n").lower()

number_of_guesses = 10 if play_mode == "easy" else 5

while True: 
    if number_of_guesses > 0: 
        take_a_guess = int(input("Please type your guess.\n"))

        if take_a_guess == number_to_guess: 
            print(f"Correct! The number is {number_to_guess}")
            break
        elif take_a_guess > number_to_guess: 
            number_of_guesses -= 1
            print(f"Too high. {number_of_guesses} guesses left")

        elif take_a_guess < number_to_guess: 
            number_of_guesses -= 1
            print(f"Too low. {number_of_guesses} guesses left")
    else: 
        print("You're out of guesses!")
        break