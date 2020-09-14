from datetime import timedelta,datetime

import airflow
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator

def print_name():
    print('Lav')

def print_city():
    print('GZB')

default_args = {
    'owner':'airflow',
    'start_date':airflow.utils.dates.days_ago(2),
    'depends_on_past':False,
    'retries':0
}

dag = DAG(
    'python_code_lav',
    default_args=default_args,
    description='First DAG',
    catchup=False,
    schedule_interval='@once'
)

t1=DummyOperator(
    task_id='start',
    dag=dag
)

# t2=PythonOperator(
#     task_id='print name',
#     python_callable = print_name,
#     dag=dag
# )


# t3=PythonOperator(
#     task_id='print city',
#     python_callable = print_city,
#     dag=dag
# )

t4=DummyOperator(
    task_id='end',
    dag=dag
)

# t1 >> t2 >> t3 >> t4
t1 >> t4