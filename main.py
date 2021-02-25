import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
alphabet = {row.letter: row.code for (index, row) in data.iterrows()}


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
to_translate = input("Please enter the word you want to translate into NATO Alphabet.\n").upper()
print([alphabet[letter] for letter in to_translate])