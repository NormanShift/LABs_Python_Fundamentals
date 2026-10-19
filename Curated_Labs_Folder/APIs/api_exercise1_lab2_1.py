from api_client import get_json

geocoding_url = "https://geocoding-api.open-meteo.com/v1/search"

params = {
    "name": "Stockholm",
    "count": 1
}

data = get_json(geocoding_url, params=params) # Here we initialize params with Stockholm and count.

# Print the complete respnse first
print(data)

if data is not None and data.get("results"):
    city = data["results"][0]

    latitude = city["latitude"]
    longitude = city["longitude"]

    print(f"Latitude: {latitude}")
    print(f"Longitude: {longitude}")

    forecast_url = "https://api.open-meteo.com/v1/forecast"

weather_params = {
    "latitude": latitude,
    "longitude": longitude,
    "current": "temperature_2m,wind_speed_10m"
}

weather_data = get_json(forecast_url, params=weather_params)

# Print the complete response first
print(weather_data)

if weather_data is not None:
    current = weather_data["current"]
    units = weather_data["current_units"]

    temperature = current["temperature_2m"]
    wind_speed = current["wind_speed_10m"]

    temperature_unit = units["temperature_2m"]
    wind_speed_unit = units["wind_speed_10m"]

    print(f"Temperature: {temperature}{temperature_unit}")
    print(f"Wind speed: {wind_speed} {wind_speed_unit}")
else:
    print("Could not retrieve the weather.")


