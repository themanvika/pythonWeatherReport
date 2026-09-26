# Weather Report Project
# GitHub: https://github.com/themanvika/pythonWeatherReport.git

import requests

city = input("Enter a city (default: Cheonan): ").strip()

if city == "":
    city = "Cheonan"

print(f"\nSearching for {city}...")

url = "https://geocoding-api.open-meteo.com/v1/search"

params = {
    "name": city,
    "count": 1,
    "language": "en",
    "format": "json"
}

response = requests.get(url, params=params)
data = response.json()

if "results" not in data:
    print("City not found.")
else:
    location = data["results"][0]

    city_name = location["name"]
    latitude = location["latitude"]
    longitude = location["longitude"]
    country = location.get("country", "")

    print(f"Location: {city_name}, {country}")
    print(f"Latitude: {latitude}")
    print(f"Longitude: {longitude}")