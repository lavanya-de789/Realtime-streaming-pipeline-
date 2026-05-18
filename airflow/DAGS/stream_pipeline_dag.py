from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
'data_stream_pipeline',
start_date=datetime(2025,1,1),
schedule='@daily',
catchup=False
) as dag:

    check_kafka=BashOperator(
        task_id='check_kafka',
        bash_command='docker ps'
    )

    run_stream=BashOperator(
        task_id='run_stream',
        bash_command='spark-submit spark/stream_job.py'
    )

    validate_data=BashOperator(
        task_id='validate_data',
        bash_command='ls data/bronze'
    )

check_kafka>>run_stream>>validate_data
