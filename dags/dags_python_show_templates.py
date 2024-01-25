import datetime
import pendulum
from airflow.models.dag import DAG
from airflow.operators.bash import BashOperator
from airflow.decorators import task


with DAG(
    dag_id="dags_python_show_templates",
    schedule="0 10 * * *",
    start_date=pendulum.datetime(2024, 1, 11, tz="Asia/Seoul"),
    catchup=True,
) as dag:
    
    @task(task_id='python_task')
    def show_templates(**kwargs):
        from pprint import pprint
        pprint(kwargs)

    show_templates()