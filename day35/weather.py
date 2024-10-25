import os

import requests

MY_LAT = 23.810331
MY_LONG = 90.412521

API_KEY = os.environ.get("OWM_API_KEY")

parameters = {"lat": MY_LAT, "lon": MY_LONG, "appid": API_KEY, "cnt": 4}

response = requests.get(
    url="https://api.openweathermap.org/data/2.5/forecast", params=parameters
)

response.raise_for_status()

data = response.json()


for n in range(parameters["cnt"]):
    data_weather = data["list"][n]["weather"]
    print(data["list"][n])
    print()

    if int(data_weather[0]["id"]) < 700:
        print("Bring an umbrella. Its gonna Rain money!")
        # break
