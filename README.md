# Workout Tracker

Welcome to the Workout Tracker project! This application helps users log their workouts by querying exercise data from the Nutritionix API and storing this data in a Google Sheet using the Sheety API. 

## Features

- **Exercise Logging**: Record and track exercise details such as exercise name, duration, and calories burned.
- **API Integration**: Fetch real-time exercise data from the Nutritionix API.
- **Google Sheets Integration**: Save and manage workout logs in a Google Sheet via the Sheety API.
- **Real-time Updates**: Automatically update your workout logs with accurate exercise data.

## Project Structure

The project consists of the following file:

- **`main.py`**: The main script for logging workouts. It handles user input, queries the Nutritionix API for exercise data, and sends the data to a Google Sheet using the Sheety API.

## Installation

To set up this project, follow these steps:

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/workout-tracker.git
    ```

2. **Navigate to the Project Directory**:
    ```bash
    cd workout-tracker
    ```

3. **Install Required Packages**:
    Ensure Python is installed on your system. Install the necessary Python packages using pip:
    ```bash
    pip install requests
    ```

4. **Configure API Keys**:
   - Open `main.py` and replace the placeholders for `APP_ID`, `API_KEY`, and `SHEETY_URL` with your actual API credentials and URLs.

## Usage

1. **Run the Script**:
    To start logging workouts, execute the script:
    ```bash
    python workout_tracker.py
    ```

2. **Input Exercise Details**:
    - When prompted, enter the name of the exercise you performed.
    - The script will query the Nutritionix API for exercise details and log this data to your Google Sheet.

## File Format

The workout data is logged to a Google Sheet with the following columns:

- **Date**: The date when the exercise was performed.
- **Time**: The time of the exercise.
- **Exercise**: The name of the exercise.
- **Duration**: The duration of the exercise in minutes.
- **Calories**: The calories burned during the exercise.


## Important Notes

- Ensure you keep your API keys and credentials secure and avoid exposing them in public repositories.
- Replace all placeholder values in the script with your actual API credentials before running the script.


