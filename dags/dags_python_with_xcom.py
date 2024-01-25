import pendulum
from airflow.models.dag import DAG
from airflow.operators.bash import BashOperator
from airflow.decorators import dag, task

with DAG(
    dag_id="dags_python_with_xcom",
    schedule="0 2 * * 6#2",
    start_date=pendulum.datetime(2024, 1, 1, tz="Asia/Seoul"),
    catchup=False,
) as dag:
    @task(task_id='python_xcom_push_task1')
    def xcom_push1(**kwargs):
        ti = kwargs.get('ti')
        ti.xcom_push(key='result1' , value='value_1')
        ti.xcom_push(key='result2' , value=[1,2,3])
    
    @task(task_id='python_xcom_push_task2')
    def xcom_push2(**kwargs):
        ti = kwargs.get('ti')
        ti.xcom_push(key='result1' , value='value_2')
        ti.xcom_push(key='result2' , value=[5,6,7,8])
    
    @task(task_id='python_xcom_pull_task')
    def xcom_pull(**kwargs):
        ti = kwargs.get('ti')
        value1 = ti.xcom_pull(key='result1') #예상 출력은 같은 key 값중 가장 늦게 저장된 xcom_push2() 의 value_2
        value2 = ti.xcom_pull(key='result2' , task_ids='python_xcom_push_task1') # 예상 출력은 pytoh_xcom_push_task1 의 result2 인 [1,2,3]
        print(value1)
        print(value2)
    
    xcom_push1() >> xcom_push2() >> xcom_pull()
    

    @task(task_id='python_xcom_push_by_return')
    def xcom_push_result(**kwargs):
        return 'Success' # 기본적으로 PythonOperator 에서 return 을 하게 되면 return_value 로 xcom 에 저장을 하게 됨. 

    @task(task_id='python_xcom_pull_ti1')
    def xcom_pull_ti1(**kwargs):
        ti = kwargs.get('ti')
        value1 = ti.xcom_pull(task_ids='python_xcom_push_by_return') # PythonOperator 에서 return_value 로 저장된 xcom 값을 가져오기. 
        print('xcom_pull 메소드로 직접 찾은 리턴 값:' + value1)

    @task(task_id='python_xcom_pull_ti2')
    def xcom_pull_ti2(status, **kwargs):
        print('함수 입력 값으로 받은 값: ' + status)

    #아래 흐름도의 예상 시나리오 
    python_xcom_push_by_return = xcom_push_result()  #xcom_push_result() 함수를 호출하면서 xcom 을 먼저 적재
    xcom_pull_ti2(python_xcom_push_by_return)        #xcom_push_result() 호출 후에 xcom_pull_ti2 를 호출하는 로직이며, 인자로 받는 resutn 값을 출력
    python_xcom_push_by_return >> xcom_pull_ti1()    #또한 xcom_push_result() 후 xcom_pull_ti1 도 호출하게 되고, 여기서는 xcom 값을 가지고 출력
