from weather import get_coordinates, get_forecast, get_noaa_endpoints

def test_coordinates():
    assert get_coordinates("Gardner,MA") == (42.5763523,-71.9952737)

def test_get_endpoints():
    assert get_noaa_endpoints(42.5763523,-71.9952737) == "https://api.weather.gov/gridpoints/BOX/38,105/forecast"