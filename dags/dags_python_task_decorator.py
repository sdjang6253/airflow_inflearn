import datetime
import pendulum
from airflow.models.dag import DAG
from airflow.operators.python import PythonOperator
from airflow.decorators import dag, task

with DAG(
    dag_id="dags_python_task_decorator",
    schedule="0 2 * * 1",
    start_date=pendulum.datetime(2024, 1, 1, tz="Asia/Seoul"),
    catchup=False,
) as dag:
    @task(task_id="python_task_1")
    def print_context(some_input):
        print(some_input)
        
    @task(task_id="python_task_2")
    def print_context2(some_input):
        print('이건 두번째에요!' + some_input)

    python_task_1 = print_context('task_decorator 실행')
    python_task_2 = print_context2('두우번째')

python_task_1 >> python_task_2