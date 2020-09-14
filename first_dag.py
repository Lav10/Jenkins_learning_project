from datetime import timedelta

import airflow
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator

default_args = {
    'owner':'airflow',
    'start_date':airflow.utils.dates.days_ago(2),
    'depends_on_past':False,
    'retries':0
}

dag = DAG(
    'lav',
    default_args=default_args,
    description='First DAG',
    catchup=False,
    schedule_interval='@once'
)

t1=DummyOperator(
    task_id='start',
    dag=dag
)

t2=DummyOperator(
    task_id='end',
    dag=dag
)


# t1.set_downstream(t2)
# t3.set_upstream(t2)

t1 >> t2