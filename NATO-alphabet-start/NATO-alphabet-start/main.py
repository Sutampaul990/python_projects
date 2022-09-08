import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")


#TODO 1. Create a dictionary in this format:

new_dict = {row.letter:row.code for (index, row) in data.iterrows()}


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

user = input("Enter a Word : ").upper()
output = [new_dict[letter] for letter in user]
print(output)