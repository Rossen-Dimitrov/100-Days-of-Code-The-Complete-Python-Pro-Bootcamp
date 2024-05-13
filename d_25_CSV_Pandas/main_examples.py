# import csv
#
# degrees = []
# with open('weather_data.csv') as file:
#     w_data = csv.DictReader(file)
#
#     for row in w_data:
#         degrees.append(int(row['temp']))
#
# print(degrees)
#

import pandas
data = pandas.read_csv('weather_data.csv')
# temp_list = data['temp'].to_list()
# print(data['temp'].mean())
# print(data['temp'].max())
# print(data['temp'].min())
# print(sum(temp_list)/len(temp_list))

# print(data[data.temp == data.temp.max()]) # filter by high day temp
monday = data[data.day == 'Monday']
print(monday.temp[0] * (9 / 5) + 32) # °F = °C × (9/5) + 32
