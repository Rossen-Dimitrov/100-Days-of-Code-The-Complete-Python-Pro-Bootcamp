import requests
from datetime import date
USERNAME = 'rosty'
TOKEN = 'S0me3T0kenF0rTest1ng'
GRAPH_ID = 'graph-1'
headers = {
    'X-USER-TOKEN': TOKEN,
}

MY_PIXELA = 'https://pixe.la/v1/@rosty/graphs/graph-1'

pixela_endpoint = 'https://pixe.la/v1/users'

user_params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_params = {
    "id": "graph-1",
    "name": "Weight Graph",
    "unit": "Kg",
    "type": "float",
    "color": "sora"
}

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)

today = date.today().strftime("%Y%m%d")
post_params = {
    'date': today,
    'quantity': '76'
}
# response = requests.post(url=graph_endpoint, json=post_params, headers=headers)
# print(response.text)
# print(graph_endpoint)

graph_endpoint_day = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20240607"

update_params = {
    'quantity': '120',
}

# response = requests.put(url=graph_endpoint_day, json=update_params, headers=headers)
# print(graph_endpoint_day)
# print(response.text)

response = requests.delete(url=graph_endpoint_day, headers=headers)
print(response.text)