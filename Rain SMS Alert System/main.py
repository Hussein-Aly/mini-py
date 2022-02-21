import os

import requests
from twilio.http.http_client import TwilioHttpClient
from twilio.rest import Client

API_KEY = "27e2586880daa77fc1cc8cdbfc09d161"
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
ACC_SID = "AC86c55b05dc251c7b7ae59d0e27df48c6"
AUTH_TOKEN = "1ff9fb7ad1be29ee23360b2608fec859"
proxy_client = TwilioHttpClient(proxy={'http': os.environ['http_proxy'], 'https': os.environ['https_proxy']})
LAT = 48.306091
LNG = 14.286440

param = {
    "lat": LAT,
    "lon": LNG,
    "appid":  API_KEY,
    "exclude": "currently,minutely,daily"
}

response = requests.get(url=OWM_ENDPOINT, params=param)
response.raise_for_status()
data = response.json()

for time_interval in range(12):
    if data["hourly"][time_interval]["weather"][0]["id"] < 701:
        client = Client(ACC_SID, AUTH_TOKEN, http_client=proxy_client)

        message = client.messages \
            .create(
            body="It's going to rain today! bring an ☂️",
            from_='+your twilio generated number',
            to='+your number'
        )

        print(message.status)
        break

