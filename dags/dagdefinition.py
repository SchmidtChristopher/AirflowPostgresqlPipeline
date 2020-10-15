from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta

user = "Schmidt"

# default dag
default_args = {
    "owner": "Chris",
    "depends_on_past": False,
    "email": ["cjc.schmidt@gmail.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 5,
    "retry_delay": timedelta(minutes=1),
}

# Define the dag, start date and how often to run.

dag = DAG(
    dag_id="top_albums",
    default_args=default_args,
    start_date=datetime(2020, 10, 12),
    schedule_interval=timedelta(minutes=1440),
)

# task1 - fetch data
task1 = BashOperator(
    task_id="get_TopAlbums",
    bash_command="python ~/airflow/dags/src/getTopalbums.py",
    dag=dag,
)

task2 = BashOperator(
    task_id="load_data",
    bash_command="python ~/airflow/dags/src/dataload.py {{params.user}}",
    params={"user": user},
    dag=dag,
)

task1 >> task2

