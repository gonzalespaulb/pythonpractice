import random

word_list = ["noodle", "ponderosa", "columbine", "acty", "beebrush"]

#Choose a random word 

random_word = word_list[random.randint(0, len(word_list) - 1)]

# Ask the user to guess a letter and assign their answer to a variable guess

word_progress = []

for letter in range(len(random_word)): 
    word_progress += "_"

print(random_word)

while True:

    if "_" in word_progress: 
    
        guess = input("What is your next letter?\n")

        for i in range(len(random_word)): 

            if random_word[i] == guess: 
                word_progress[i] = guess
                print(word_progress)
                print(f"{guess} is in the word!")
            else: 
                print("Guess again")

    else: 
        print("You guessed the word!")
        break

    

# Check if the letter from the guess is a letter in the chosen word
