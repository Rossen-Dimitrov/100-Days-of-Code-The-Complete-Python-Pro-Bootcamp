# # new_list = [n * 2 for n in range(1, 5)]
# # print(new_list)
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# new_num = [n * n for n in numbers]
# print(new_num)

# text = 'what is the Airspeed Velocity of the unladen swallow'
# new_dict = {word: len(word) for word in text.split()}
# print(new_dict)
"""
{"Monday": 4, "Tuesday": 5, "Wednesday": 10, "Thursday": 11, "Friday": 13}
"""
# whether_c = eval(input())
#
# whether_f = {print(day, (t * (9 / 5) + 32)) for (day, t) in whether_c.items()}



student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

