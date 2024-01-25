import pendulum
from airflow.models.dag import DAG
from airflow.operators.bash import BashOperator
from airflow.decorators import dag, task

with DAG(
    dag_id="dags_python_template_macro",
    schedule="0 2 * * 6#2",
    start_date=pendulum.datetime(2024, 1, 1, tz="Asia/Seoul"),
    catchup=False,
) as dag:
   
    #START_DATE : 2주전 월요일 , END_DATE : 2주전 토요일
    bash_task_2 = BashOperator(
        task_id='bash_task_2',
        env={'START_DATE':'{{ (data_interval_end.in_timezone("Asia/Seoul") - macros.dateutil.relativedelta.relativedelta(days=19)) | ds}}',
             'END_DATE' : '{{ (data_interval_end.in_timezone("Asia/Seoul") - macros.dateutil.relativedelta.relativedelta(days=14)) | ds}}'
            },
        bash_command='echo "START_DATE: $START_DATE" && echo "END_DATE: $END_DATE"'

    )

with DAG(
    dag_id="dags_python_template_macro2",
    schedule="10 0 L * *",
    start_date=pendulum.datetime(2024, 1, 1, tz="Asia/Seoul"),
    catchup=False,
) as dag2:
    #START_DATE : 전월 말일 , END_DATE : 1일 전
    bash_task_1 = BashOperator(
        task_id='bash_task_1',
        env={'START_DATE':'{{ data_interval_start.in_timezone("Asia/Seoul") | ds}}',
             'END_DATE' : '{{ (data_interval_end.in_timezone("Asia/Seoul") - macros.dateutil.relativedelta.relativedelta(days=1)) | ds}}'
            },
        bash_command='echo "START_DATE: $START_DATE" && echo "END_DATE:$END_DATE"'

    )

##이렇게 하면, airflow 화면에는 DAG 이 두개로 나오게 됩니다!
##즉 .py 하나당 DAG 하나!