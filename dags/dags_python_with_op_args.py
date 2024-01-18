import datetime
import pendulum
from airflow.models.dag import DAG
from airflow.operators.python import PythonOperator
from airflow.decorators import dag, task
from common.common_func import regist

with DAG(
    dag_id="dags_python_with_op_args",
    schedule="30 6 * * 1",
    start_date=pendulum.datetime(2024, 1, 1, tz="Asia/Seoul"),
    catchup=False,
) as dag:
    py_t1 = PythonOperator(
        task_id='py_t1',
        python_callable=regist,
        op_args=['sdjang' , 'man' , 'kr' , 'seoul' ]
    )
    py_t1