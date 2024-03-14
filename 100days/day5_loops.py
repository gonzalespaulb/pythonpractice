import string
import random

letters = []
symbols = []
numbers = []
password = []
# How many letters
num_of_letters = int(input("How many letters?\n"))

# How many symbols
num_of_symbols = int(input("How many symbols?\n"))

# How many numbers
num_of_numbers = int(input("How many numbers?\n"))

next_pick = [letters, symbols, numbers]

# Generate string

all_letters = list(string.ascii_letters)
all_punctuations = list(string.punctuation)
total_char = num_of_letters + num_of_symbols + num_of_numbers

while True: 
    letter_length = len(letters)

    if letter_length < num_of_letters:
        letters.append(all_letters[random.randint(0, len(all_letters) - 1)])
    else: 
        break

while True: 
    symbol_length = len(symbols)

    if symbol_length < num_of_symbols:
        symbols.append(all_punctuations[random.randint(0, len(all_punctuations) - 1)])
    else: 
        break

while True: 
    number_length = len(numbers)

    if number_length < num_of_numbers:
        numbers.append(random.randint(0, 9))
    else: 
        break

while True: 
    password_length = len(password)

    all_chars = letters + numbers + symbols

    random_index = random.randint(0, len(all_chars) - 1)

    random_char = all_chars[random_index]

    if password_length < total_char: 
        password.append(random_char)
        del all_chars[random_index]

    else: 
        break


random.shuffle(password)

password = ''.join(map(str, password))

print(f"Your generated password is {password}.")
