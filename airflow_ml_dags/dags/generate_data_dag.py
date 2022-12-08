import os
from datetime import datetime, timedelta

from airflow import DAG
from airflow.models import Variable
from airflow.providers.docker.operators.docker import DockerOperator
from docker.types import Mount
from airflow.utils.dates import days_ago

default_args = {
    "owner": "aitk",
    "email": ["noreply@www.ru"],
    "retries": 1,
    "retry_delay": timedelta(minutes=10),
}

with DAG(
    'generate_data',
    default_args=default_args,
    schedule_interval='@daily',
    start_date=days_ago(10),
) as dag:
    generate = DockerOperator(
        image='airflow-generate-data',
        command='--out-dir /data/raw/{{ ds }}',
        task_id='docker-airflow-generate-data',
        do_xcom_push=False,
        network_mode='bridge',
        auto_remove=True,
        mounts=[Mount(source='/home/usert/mhw03/data/', target='/data', type='bind')]
    )

    generate
