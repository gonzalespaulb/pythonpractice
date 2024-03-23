import random

word_list = ["noodle", "ponderosa", "columbine", "acty", "beebrush"]

#Choose a random word 

# random_word = word_list[random.randint(0, len(word_list) - 1)]
random_word = random.choice(word_list)

# Ask the user to guess a letter and assign their answer to a variable guess

word_progress = []
lives = 9

for letter in range(len(random_word)): 
    word_progress += "_"

print(word_progress)

while True:

    if lives <= 0: 
        print("You lost")
        break

    if "_" in word_progress: 
    
        guess = input("What is your next letter?\n").lower()

        for i in range(len(random_word)): 

            if random_word[i] == guess: 
                word_progress[i] = guess

        if not guess in random_word: 
            print("Guess again")
            lives -= 1

        print(word_progress)

    else: 
        print("You guessed the word!")
        break

    

# Check if the letter from the guess is a letter in the chosen word
