from extract_weather import extract_weather
from load_to_gcs import upload_to_gcs
from load_to_bigquery import load_json_to_bigquery

def run_pipeline():
    file_path = extract_weather()
    upload_to_gcs(file_path)
    load_json_to_bigquery(file_path)

if __name__ == "__main__":
    run_pipeline()