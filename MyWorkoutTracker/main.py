import requests
from datetime import datetime as dt

APP_ID = "f42c258c"
API_KEY = "a9abe0e211f305403044bd0e5fd0d422"

exercise_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}
exercise_url = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_body = {
    "query": input("What Exercise did you do? ")
}

exercise_response = requests.post(url=exercise_url, headers=exercise_headers, json=exercise_body)
print(exercise_response.json())

for row in exercise_response.json()["exercises"]:
    duration = round(row["duration_min"])
    calories = round(row["nf_calories"])
    activity = row["name"].title()

    sheety_url = "https://api.sheety.co/76c41cb17dd9d9bb3b61c30e3e3646ab/myWorkouts/workouts"

    today = dt.now()
    today_date = today.strftime("%d/%m/%Y")
    today_time = today.strftime("%H:%M:%S")
    print(today_time)

    sheety_headers = {
        "Authorization": "Bearer blahblahblah"
    }

    sheety_body = {
        "workout": {
            "date": today_date,
            "time": today_time,
            "exercise": activity,
            "duration": duration,
            "calories": calories
        }
    }

    sheety_response = requests.post(url=sheety_url, json=sheety_body, headers=sheety_headers)
    print(sheety_response)

    print(sheety_response.text)

