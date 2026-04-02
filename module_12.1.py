
import requests


request = "https://api.chucknorris.io/jokes/random"
response = requests.get(request)

response = response.json()

print(response['value'])

