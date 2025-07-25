from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from  clean import pre_process
from filter import filter_data
default_args = {
    "owner": "airflow-rohith",
    "start_date": datetime(2025, 7, 23),  # Fixed typo from datatime to datetime
}

with DAG(
    dag_id='test_dag',
    default_args=default_args,
    schedule_interval='@daily',

) as dag:
     #task1-check File
    check_file = BashOperator(
        task_id='check_file',
        bash_command="ls ~/ip_files/Life_expectancy.csv",  # Changed 'mokar' to valid shell command
        retries=2,
        retry_delay=timedelta(seconds=15)  # Fixed typo: retry-delay -> retry_delay
    )

     #task2-clean
    pre_process1=PythonOperator(
         task_id='pre_process',
         python_callable=pre_process
     )

     #task3-Filter the data
    filter_data1=PythonOperator(
        task_id='filter_data1',
        python_callable=filter_data
    )

    check_file>> pre_process1>>filter_data1