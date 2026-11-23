"""Log a workout described in plain English to a Google Sheet.

The description is sent to the Nutritionix natural-language exercise API, which
returns the exercise name, duration and calories burned. Each exercise is then
added as a row to a Google Sheet through the Sheety API.

Credentials are read from environment variables (see .env.example).
"""
import datetime as dt
import os
import sys

import requests

NUTRITIONIX_URL = "https://trackapi.nutritionix.com/v2/natural/exercise"

APP_ID = os.environ.get("NUTRITIONIX_APP_ID")
API_KEY = os.environ.get("NUTRITIONIX_API_KEY")
SHEETY_URL = os.environ.get("SHEETY_URL")
SHEETY_TOKEN = os.environ.get("SHEETY_TOKEN")


def check_config():
    missing = [
        name
        for name, value in {
            "NUTRITIONIX_APP_ID": APP_ID,
            "NUTRITIONIX_API_KEY": API_KEY,
            "SHEETY_URL": SHEETY_URL,
            "SHEETY_TOKEN": SHEETY_TOKEN,
        }.items()
        if not value
    ]
    if missing:
        sys.exit(f"Missing environment variables: {', '.join(missing)}")


def parse_exercises(query):
    """Ask Nutritionix to turn a sentence like 'ran 5k and swam 20 minutes' into exercises."""
    headers = {"x-app-id": APP_ID, "x-app-key": API_KEY}
    response = requests.post(NUTRITIONIX_URL, json={"query": query}, headers=headers, timeout=15)
    response.raise_for_status()
    return response.json()["exercises"]


def log_exercise(exercise, now):
    """Add one exercise as a row in the Google Sheet."""
    body = {
        "workout": {
            "date": now.strftime("%d/%m/%Y"),
            "time": now.strftime("%H:%M:%S"),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }
    headers = {"Authorization": f"Bearer {SHEETY_TOKEN}"}
    response = requests.post(SHEETY_URL, json=body, headers=headers, timeout=15)
    response.raise_for_status()


def main():
    check_config()
    query = input("Tell me which exercises you did: ")
    now = dt.datetime.now()

    exercises = parse_exercises(query)
    if not exercises:
        print("No exercises recognised. Try something like 'ran 3 miles'.")
        return

    for exercise in exercises:
        log_exercise(exercise, now)
        print(f"Logged {exercise['name']}: {exercise['duration_min']} min, {exercise['nf_calories']} kcal")


if __name__ == "__main__":
    main()
