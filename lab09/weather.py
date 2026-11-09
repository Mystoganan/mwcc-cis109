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
        "User-Agent": "MWCC-Melanson"
    }

    response = requests.get(
        url,
        params=params,
        headers=headers
    )

    data = response.json()[0]


    print(f"Status Code: {response.status_code}")
    print(f"Lattitude: {data['lat']}")
    print(f"Longitude: {data['lon']}")

    return (data['lat'], data['lon'])

def get_noaa_endpoints(lat,lon):
    url = f"https://api.weather.gov/points/{lat},{lon}"

    headers = {
        "User-Agent": "MWCC-Melanson"
    }

    response = requests.get(
        url,
        headers=headers
    )

    data = response.json()

    print(data["properties"]["forecast"])

    return data["properties"]["forecast"]

def get_forecast(url):
    response = requests.get(url)
    data = response.json()["properties"]["periods"]

    for period in data:
        print(period["name"])

get_coordinates("Gardner,MA")
#get_noaa_endpoints("42.5763523","-71.9952737")
#get_forecast("https://api.weather.gov/gridpoints/BOX/38,105/forecast")