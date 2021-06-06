import requests

response = requests.get(
    "http://api.openweathermap.org/data/2.5/weather?q=moscow&appid=fd7a000568216df01e6907e2b727ef63")
data_json = response.json()
cels = round(data_json["main"]["feels_like"] / 15.5)
print(cels)
