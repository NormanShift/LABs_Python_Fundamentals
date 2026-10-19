from api_client import get_json


def find_city(name):
    geocoding_url = "https://geocoding-api.open-meteo.com/v1/search"

    params = {
        "name": name,
        "count": 1
    }

    data = get_json(geocoding_url, params=params)

    if data is not None and data.get("results"):
        return data["results"][0]

    return None


def get_weather(latitude, longitude):
    forecast_url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,wind_speed_10m"
    }

    data = get_json(forecast_url, params=params)

    if data is not None:
        return data

    return None


city_name = input("Enter a city: ").strip()
city = find_city(city_name)

if city is not None:
    latitude = city["latitude"]
    longitude = city["longitude"]

    weather = get_weather(latitude, longitude)

    if weather is not None:
        current = weather["current"]
        units = weather["current_units"]

        temperature = current["temperature_2m"]
        wind_speed = current["wind_speed_10m"]

        temperature_unit = units["temperature_2m"]
        wind_speed_unit = units["wind_speed_10m"]

        print(
            f'{city["name"]}, {city["country"]}: '
            f"{temperature}{temperature_unit}, "
            f"wind {wind_speed} {wind_speed_unit}"
        )
    else:
        print("Could not retrieve the weather.")
else:
    print("The city could not be found.")