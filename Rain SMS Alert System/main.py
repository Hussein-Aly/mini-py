import requests

API_KEY = "27e2586880daa77fc1cc8cdbfc09d161"
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
LAT = 48.306091
LNG = 14.286440

param = {
    "lat": LAT,
    "lon": LNG,
    "appid":  API_KEY
}

response = requests.get(url=OWM_ENDPOINT, params=param)
response.raise_for_status()
data = response.json()
print(data["hourly"])




