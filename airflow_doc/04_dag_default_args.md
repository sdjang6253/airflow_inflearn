###10-2
Airflow 에는 DAG 에 기본적으로 선언되어 있는 파라미터가 있고, BaseOperator 에 선언되어 있는 파라미터가 있다. 

이를 확인하는 방법은, Document 들어가서 확인을 해보면 되며 SLA 적용을 할때 많이 고민을 했던 부분이라 추가를 하게 되었다. 

SLA 를 적용하는 변수는 BaseOperator 에 파라미터 이기 때문에, 
'''
with DAG (
    dag_id = 'XXX'
    schedule = '1 * * * * *'
    default_args={
        'sla'=timadelta(minutes=1)
    }
)
'''
이런 식으로 써야 한다. 그런데, SLA 의 실패 했을때 행위는 sla_miss_callback 에 정의를 하는데 이는 DAG 파라미터 이기 때문에 , 

'''
with DAG (
    dag_id = 'XXX'
    schedule = '1 * * * * *'
    default_args={
        'sla'=timadelta(5 minutes)
    }
    sla_miss_callback = missFn
)
'''
처럼 써주어야 한다. 

DAG 정의 : https://airflow.apache.org/docs/apache-airflow/stable/_modules/airflow/models/dag.html#DAG
BaseOperator 정의 : https://airflow.apache.org/docs/apache-airflow/stable/_modules/airflow/models/baseoperator.html#BaseOperator