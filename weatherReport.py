# Weather Report Project
# GitHub: https://github.com/themanvika/pythonWeatherReport.git

import requests
import json
from datetime import datetime

city = input("Enter a city (default: Cheonan): ").strip()

if city == "":
    city = "Cheonan"

print("\n🌤 Weather Forecast (Open-Meteo API)")
print("3-day weather information\n")

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
    country = location.get("country", "")
    latitude = location["latitude"]
    longitude = location["longitude"]

    print(f"📍 {city_name}, {country}")
    print(f"Latitude: {latitude}")
    print(f"Longitude: {longitude}")

    # 2. Forecast
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

    print("\n" + "=" * 50)
    print(f"🌤 {city_name} 3-Day Weather Forecast")
    print("=" * 50)

    for i in range(len(daily["time"])):
        date_obj = datetime.strptime(daily["time"][i], "%Y-%m-%d")
        formatted_date = date_obj.strftime("%m.%d")

        print(f"\n📅 Day {i + 1} ({formatted_date})")
        print("-" * 40)
        print(f"🌡 Max temperature: {daily['temperature_2m_max'][i]}°C")
        print(f"❄ Min temperature: {daily['temperature_2m_min'][i]}°C")
        print(f"🌧 Rain probability: {daily['precipitation_probability_max'][i]}%")

    # 3. Save as JSON
    save_choice = input("\nSave weather information as JSON? (y/n): ").strip().lower()

    if save_choice == "y":
        file_name = f"{city_name}_weather.json"

        save_data = {
            "city": city_name,
            "country": country,
            "latitude": latitude,
            "longitude": longitude,
            "forecast": daily
        }

        with open(file_name, "w", encoding="utf-8") as file:
            json.dump(save_data, file, ensure_ascii=False, indent=4)

        print(f"Weather information saved to {file_name}")
    else:
        print("Weather information was not saved.")