from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.dummy import DummyOperator
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'retries': 1,
    'start_date': datetime(2024, 6, 1),
}

with DAG(
    dag_id='dag_teste',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False,
) as dag:

    start = DummyOperator(task_id='start', dag=dag)
    end = DummyOperator(task_id='end', dag=dag)


    start >> end