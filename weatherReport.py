# Weather Report Project
# GitHub: https://github.com/themanvika/pythonWeatherReport.git

import requests

city = input("Enter a city (default: Cheonan): ").strip()

if city == "":
    city = "Cheonan"

print(f"\nSearching for {city}...")

# 1. Geocoding
geo_url = "https://geocoding-api.open-meteo.com/v1/search"

geo_params = {
    "name": city,
    "count": 1,
    "language": "en",
    "format": "json"
}

geo_response = requests.get(geo_url, params=geo_params)
geo_data = geo_response.json()

if "results" not in geo_data:
    print("City not found.")
else:
    location = geo_data["results"][0]

    city_name = location["name"]
    latitude = location["latitude"]
    longitude = location["longitude"]

    print(f"Location found: {city_name}")
    print(f"Latitude: {latitude}")
    print(f"Longitude: {longitude}")

    # 2. Weather forecast
    weather_url = "https://api.open-meteo.com/v1/forecast"

    weather_params = {
        "latitude": latitude,
        "longitude": longitude,
        "daily": "temperature_2m_max,temperature_2m_min,precipitation_probability_max",
        "forecast_days": 3,
        "timezone": "auto"
    }

    weather_response = requests.get(weather_url, params=weather_params)
    weather_data = weather_response.json()

    daily = weather_data["daily"]

    print("\n3-Day Weather Forecast")

    for i in range(len(daily["time"])):
        print(f"\nDate: {daily['time'][i]}")
        print(f"Max temperature: {daily['temperature_2m_max'][i]}°C")
        print(f"Min temperature: {daily['temperature_2m_min'][i]}°C")
        print(f"Rain probability: {daily['precipitation_probability_max'][i]}%")