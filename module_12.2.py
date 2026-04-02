import requests

api = "c9171278703913210b2a5a2d1f13408f"
city = input("Enter municipality: ")
request = (f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}&units=metric")

response = requests.get(request)
response = response.json()

weather = response["weather"][0]["description"]
temperature = response["main"]["temp"]

print(f"The current weather of {city} is {weather} and {temperature} Celsius.")

