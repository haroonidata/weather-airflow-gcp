import requests
import json
from datetime import datetime
import os 

CITIES = [
    "Manchester",
    "London",
    "Birmingham",
    "Leeds",
    "Liverpool",
    "Glasgow",
    "Edinburgh",
    "Cardiff",
    "Bristol",
    "Sheffield"
]
API_KEY = "64d71a443ead2cc8993288c7f8b49d2f"
#CITY = "Manchester"
#URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

def extract_weather():
    all_weather = []

    for city in CITIES:
         url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

         response = requests.get(url)
         response.raise_for_status()

         data = response.json()
         all_weather.append(data)

    os.makedirs("../data", exist_ok=True)

    filename = f"../data/weather_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

    with open(filename, "w") as f:
        json.dump(all_weather, f)

    print(f"Saved file: {filename}")

    return filename

if __name__ == "__main__":
    extract_weather()
