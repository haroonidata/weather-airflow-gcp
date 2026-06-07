import json
from datetime import datetime, UTC
from google.cloud import bigquery

PROJECT_ID = "weather-ml-project-498711"
DATASET_ID = "weather_data"
TABLE_ID = "raw_weather"

def load_json_to_bigquery(local_file_path):
    client = bigquery.Client(project=PROJECT_ID)
    table_id = f"{PROJECT_ID}.{DATASET_ID}.{TABLE_ID}"

    with open(local_file_path, "r") as f:
        weather_list = json.load(f)

    # If file has 1 city as a dict, convert it to a list
    if isinstance(weather_list, dict):
        weather_list = [weather_list]

    rows = []

    for data in weather_list:
        weather_time = datetime.fromtimestamp(data["dt"], UTC)
        ingestion_time = datetime.now(UTC)

        rows.append({
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "weather": data["weather"][0]["description"],
            "wind_speed": data["wind"]["speed"],
            "weather_time": weather_time.isoformat(),
            "ingestion_time": ingestion_time.isoformat()
        })

    errors = client.insert_rows_json(table_id, rows)

    if errors:
        raise Exception(errors)

    print(f"Loaded {len(rows)} rows into BigQuery")