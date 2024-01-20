import datetime
import pendulum
from airflow.models.dag import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator


with DAG(
    dag_id="dags_bash_with_template",
    schedule="0 10 * * *",
    start_date=pendulum.datetime(2024, 1, 1, tz="Asia/Seoul"),
    catchup=False,
) as dag:
    bash_t1 = BashOperator(
        task_id="bash_t1",
        bash_command='echo "data_interval_end: {{ data_interval_end }}"',
    )

    bash_t2 = BashOperator(
        task_id="bash_t2",
        env={
            'START_DATE' : '{{data_interval_start | ds}}',
            'END_DATE' : '{{data_interval_end | ds }}',
        },
        bash_command='echo $START_DATE && echo $END_DATE'
    )
bash_t1 >> bash_t2