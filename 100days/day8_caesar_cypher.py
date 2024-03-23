import string

all_letters = list(string.ascii_lowercase)

word_to_encode = "zzz"

shift_number = 2

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

word_to_encode = encoder(word_to_encode)

print(word_to_encode)


# Also the decode