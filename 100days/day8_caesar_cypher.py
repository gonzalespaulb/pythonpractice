import string

all_letters = list(string.ascii_lowercase)

word_to_encode = input("Type a word\n")
encode_or_decode = input("Encode or decode?\n")
shift_number = int(input("How many shifts?\n"))

def caesar (word, decode_or_encode): 
    word_as_list = list(word.lower())

    for i in range(len(word_as_list)): 

        index_in_alphabet = all_letters.index(word_as_list[i])

        # Take into account the wrap around
        shift_letter_back = all_letters[(index_in_alphabet - shift_number) % 26]
        shift_letter = all_letters[(index_in_alphabet + shift_number) % 26]

        word_as_list[i] = shift_letter if decode_or_encode == "encode" else shift_letter_back

    encoded_or_decoded_word = ''.join(word_as_list)

    return encoded_or_decoded_word

encoded_or_decoded_word = caesar(word_to_encode, encode_or_decode)
print(encoded_or_decoded_word)
