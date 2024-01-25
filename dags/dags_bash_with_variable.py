import pendulum
from airflow.models.dag import DAG
from airflow.operators.bash import BashOperator
from airflow.decorators import dag, task
from airflow.models import Variable

with DAG(
    dag_id="dags_bash_with_variable",
    schedule="0 2 * * 6#2",
    start_date=pendulum.datetime(2024, 1, 1, tz="Asia/Seoul"),
    catchup=False,
) as dag:
    var_value = Variable.get("simple_key") # 이방식은 비추천 -> 이유는 airflow 는 스케쥴러가 주기적으로 dag 파일을 해석하는데, 
                                           #라이브러리를 많이 가져오면 실제 수행되는중이 아니어도 자원을 잡아 먹기 때문에 아래 방법 추천

    bash_var_1 = BashOperator(
        task_id = "bash_var_1",
        bash_command=f"echo variable:{var_value}"
    )

    bash_var_2 = BashOperator(
        task_id = 'bash_var_2',
        bash_command='echo variable:{{var.value.simple_key}}' #이방식을 추천
    )