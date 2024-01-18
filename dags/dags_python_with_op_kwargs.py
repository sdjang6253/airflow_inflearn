import datetime
import pendulum
from airflow.models.dag import DAG
from airflow.operators.python import PythonOperator
from airflow.decorators import dag, task
from common.common_func import regist2

with DAG(
    dag_id="dags_python_with_op_kwargs",
    schedule="30 6 * * 1",
    start_date=pendulum.datetime(2024, 1, 1, tz="Asia/Seoul"),
    catchup=False,
) as dag:
    py_t1 = PythonOperator(
        task_id='py_t1',
        python_callable=regist2,
        op_args=['sdjang' , 'man' , 'kr' , 'seoul'],
        op_kwargs=[{'email': 'sdjang@naver.com' , 'phone' : '010'}]
    )
    py_t1