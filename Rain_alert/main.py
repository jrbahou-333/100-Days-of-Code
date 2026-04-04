import requests
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = "AC6ac056104ef821352a9be010096fdeee"
auth_token = "ce43f0c57b263aae54acd4c3f08caa62"


url = "https://api.openweathermap.org/data/3.0/onecall"
api_key = "364693791a9d35a5de938174c4b00297"
weather_params = {
    "appid" : api_key,
    "lat": -16.9,
    "lon": 145.7,
    "exclude": "current,minutely,daily"
}
response = requests.get(url, params=weather_params)

hourly_data = response.json()["hourly"]
rain = False

for i in range(0, 12):
    code = hourly_data[i]["weather"][0]["id"]
    if code < 700:
        rain = True

if not rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="It's not going to rain today!",
        from_='+14842710546',
        to='+61 467 662 865'
    )

    print(message.status)


