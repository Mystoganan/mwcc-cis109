import json
import requests
import argparse

def get_coordinates(city):
    url = "https://nominatim.openstreetmap.org/search"

    params = {
        "q": city,
        "format": "json",
        "limit" :1
    }
    
    headers = {
        "User-Agent": "MWCC-Gorden"
    }

    response = requests.get(
        url,
        params=params,
        headers=headers
    )

    data = response.json()[0]

    return (data['lat'], data['lon'])

def get_noaa_endpoints(lat,lon):
    url = f"https://api.weather.gov/points/{lat},{lon}"

    headers = {
        "User-Agent": "MWCC-Gorden"
    }

    response = requests.get(
        url,
        headers=headers
    )

    data = response.json()

    return data["properties"]["forecast"]

def get_forecast(url):
    response = requests.get(url)
    data = response.json()["properties"]["periods"]

    return data
    
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--location", required=True, help="Location you want the forecast of (City, State)")
    parser.add_argument("-d", "--detailed", action='store_true', required=False, help="Give a detailed forecast of the current day/night")
    parser.add_argument("-w", "--week", action='store_true', required=False, help="Return a short forecast for the week")
    parser.add_argument("-a", "--average", action='store_true', required=False, help="Average temperature for the next week")
    args = parser.parse_args()

    temp_data = []

    if args.location:
        coordinates = get_coordinates(args.location)
        url = get_noaa_endpoints(coordinates)
        data = get_forecast(url)

    if args.detailed:
        for period in data:
            if period["number"] == 1:
                print(f"Current Temp:{period["temperature"]} \nForecast: {period["detailedForecast"]}")

    elif args.week:
        for period in data:
            if len(period["name"]) < 9:
                print(f"Day: {period["name"]} \nForecast: {period["shortForecast"]}")

    elif args.average:
        for period in data:
            temp_data.append(period["temperature"])
        average = sum(temp_data)/len(temp_data)
        print(f"Average Temperature for the week: {average}°F")
        
main()