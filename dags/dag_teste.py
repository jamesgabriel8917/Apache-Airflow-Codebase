from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def hello_world():
    print("Hello, Airflow!")

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 6, 1),
}

with DAG(
    dag_id='dag_teste',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False,
) as dag:
    task_hello = PythonOperator(
        task_id='hello_world_task',
        python_callable=hello_world,
    )