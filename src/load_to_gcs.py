from google.cloud import storage

BUCKET_NAME = "haroon-weather-ml-498711"

def upload_to_gcs(local_file_path):
    client = storage.Client(project="weather-ml-project-498711")
    bucket = client.bucket(BUCKET_NAME)

    file_name = local_file_path.split("/")[-1]
    blob = bucket.blob(f"raw/{file_name}")

    blob.upload_from_filename(local_file_path)

    print(f"Uploaded to gs://{BUCKET_NAME}/raw/{file_name}")
    return f"gs://{BUCKET_NAME}/raw/{file_name}"