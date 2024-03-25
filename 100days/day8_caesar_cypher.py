import string

all_letters = list(string.ascii_lowercase)

word_to_encode = input("What word to encode?\n")
shift_number = int(input("How many shifts?\n"))

# print(all_letters[26 - 1])

def encoder (word): 

    word_as_list = list(word.lower())

    for i in range(len(word_as_list)): 

        index_in_alphabet = all_letters.index(word_as_list[i])

        # Take into account the wrap around
        shifted_letter = all_letters[(index_in_alphabet + shift_number) % 26]

        word_as_list[i] = shifted_letter

    encoded_word = ''.join(word_as_list)

    return encoded_word

# Also the decode

def decoder (word): 

    word_as_list = list(word.lower())

    for i in range(len(word_as_list)): 

        index_in_alphabet = all_letters.index(word_as_list[i])

        # Take into account the wrap around
        shifted_letter = all_letters[(index_in_alphabet - shift_number) % 26]

        word_as_list[i] = shifted_letter

    decoded_word = ''.join(word_as_list)

    return decoded_word

encoded_word = encoder(word_to_encode)
print(encoded_word)
print(decoder(encoded_word))


