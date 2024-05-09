PLACEHOLDER = "[name]"

with open("Input/Letters/starting_letter.txt") as file:
    start_letter = file.read()

with open("Input/Names/invited_names.txt") as file:
    names = file.readlines()
    for n in names:
        name = n.strip()
        new_letter = start_letter.replace(PLACEHOLDER, name)
        with open(f'Output/ReadyToSend/letter_to_{name}.txt', 'w') as completed_letter:
            completed_letter.write(new_letter)

