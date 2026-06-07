terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 5.0"
    }
  }
}

provider "google" {
  project = "weather-ml-project-498711"
  region  = "europe-west2"
}

resource "google_storage_bucket" "weather_bucket" {
  name     = "haroon-weather-ml-498711"
  location = "EU"
}

resource "google_bigquery_dataset" "weather_dataset" {
  dataset_id = "weather_data"
  location   = "EU"
}