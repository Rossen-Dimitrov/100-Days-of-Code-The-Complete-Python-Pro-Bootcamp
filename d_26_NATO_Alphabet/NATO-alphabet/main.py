import pandas

nato_ab = pandas.read_csv('nato_phonetic_alphabet.csv')
nato_ab_data_frame = pandas.DataFrame(nato_ab)

#TODO 1. Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}

nato_ab_dict = {row.letter: row.code for (index, row) in nato_ab_data_frame.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

input_list = [letter.upper() for letter in input('Enter name: ')]
nato_name = [nato_ab_dict[l] for l in input_list]

print(nato_name)
