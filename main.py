import requests
import datetime as dt

# Replace these with your actual credentials
APP_ID = "Your APP ID"  # Nutritionix App ID
API_KEY = "Your API KEY"  # Nutritionix API Key

# URL for the Nutritionix API
NUTRITIONX_URL = "https://trackapi.nutritionix.com/v2/natural/exercise"

# Replace this with your actual Sheety URL
SHEETY_URL = "Your SHEETY URL"

# User input for the exercise performed
User_input = input("Tell me which exercise you did:\n")

# Headers for the Nutritionix API request
headers = {
    "x-app-id": APP_ID,  # App ID for Nutritionix API
    "x-app-key": API_KEY  # API Key for Nutritionix API
}

# Parameters for the Nutritionix API request
params = {
    "query": query  # User-provided exercise query
}

# Make a POST request to Nutritionix API
post = requests.post(url=NUTRITIONX_URL, json=params, headers=headers)

# Print the JSON response from Nutritionix API for debugging
print(post.json())

# Extract exercise details from the response
workout = (post.json())["exercises"][0]["name"]  # Name of the exercise
duration = (post.json())["exercises"][0]["duration_min"]  # Duration in minutes
calories = (post.json())["exercises"][0]["nf_calories"]  # Calories burned

# Get current date and time
now = dt.datetime.now()
date = now.date().strftime("%d/%m/%Y")  # Format date as DD/MM/YYYY
time = now.time().strftime("%H:%M:%S")  # Format time as HH:MM:SS

# Prepare the body for the Sheety API request
body = {
    "workout": {
        "date": date,  # Date of the workout
        "time": time,  # Time of the workout
        "exercise": workout,  # Name of the exercise
        "duration": duration,  # Duration of the exercise
        "calories": calories  # Calories burned
    }
}

# Headers for the Sheety API request
header = {
    "Authorization": "Bearer YOUR_SHEETY_API_KEY"  # Authorization header for Sheety API
}

# Make a POST request to Sheety API to log the workout
x = requests.post(url=SHEETY_URL, json=body, headers=header)

# Print the response from Sheety API for debugging
print(x.text)
