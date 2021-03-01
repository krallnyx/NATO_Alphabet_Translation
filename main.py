import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
alphabet = {row.letter: row.code for (index, row) in data.iterrows()}


def generate_phonetic():
    to_translate = input("Please enter the word you want to translate into NATO Alphabet.\n").upper()
    try:
        output = [alphabet[letter] for letter in to_translate]
    except KeyError:
        print("Please enter a valid word, only letters in the alphabet are allowed")
        generate_phonetic()
    else:
        print(output)


generate_phonetic()
