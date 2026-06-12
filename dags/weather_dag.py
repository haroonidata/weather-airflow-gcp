from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import sys
from weather_pipeline import run_pipeline

sys.path.append("/opt/airflow/src")

with DAG(
    dag_id="weather_pipeline_dag",
    start_date=datetime(2026, 6, 7),
    schedule="@daily",
    catchup=False,
) as dag:

    run_weather_pipeline = PythonOperator(
        task_id="run_weather_pipeline",
        python_callable=run_pipeline,
    )


sys.path.append("/opt/airflow/src")

from weather_pipeline import run_pipeline

with DAG(
    dag_id="weather_pipeline_dag",
    start_date=datetime(2026, 6, 7),
    schedule="@daily",
    catchup=False,
) as dag:

    run_weather_pipeline = PythonOperator(
        task_id="run_weather_pipeline",
        python_callable=run_pipeline,
    )