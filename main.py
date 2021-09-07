import requests
from twilio.rest import Client

# Open Weather
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "8a3cb7601d8c66334446f0daffb8cb3b"

# Twilio
account_sid = "AC4bc9d655663dcdcdbee672f007fc79d9"
auth_token = "39305dce6577d2c667967370a1afdb34"

weather_params = {
    "lat": 37.566536,
    "lon": 126.977966,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(url=OWM_Endpoint, params=weather_params)
response.raise_for_status()


weather_data = response.json()
twelve_hour_forecast = list(weather_data["hourly"][0:12])

code_list = []

for _ in range(12):
    code_list.append(twelve_hour_forecast[_]['weather'][0]['id'])

need_umbrella = False
for x in code_list:
    if x < 700:
        need_umbrella = True

if need_umbrella:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an umbrella️",
        from_='+13195058865',
        to='+821046321383'
    )
    print(message.status)