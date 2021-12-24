import requests
import json

while True:
    city = input("Enter a city and learn the weather:  ")
    apiKey = "e2c9d6beb6f8c0f0f4ac901d63f2f4ab"
    address = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&lang=tr&units=metric".format(city, apiKey)
    connect = requests.get(address)
    query = connect.json()
    weather = query["weather"][0]["description"]
    temprature = query["main"]["temp"]
    print(weather + " - " + str(temprature))

