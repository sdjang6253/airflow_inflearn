import pendulum
from airflow.models.dag import DAG
from airflow.operators.python import PythonOperator
from airflow.decorators import dag, task

with DAG(
    dag_id="dags_python_template",
    schedule="0 2 * * 1",
    start_date=pendulum.datetime(2024, 1, 1, tz="Asia/Seoul"),
    catchup=False,
) as dag:
   
    def python_function1(start_date , end_date , **kwargs):
        print(start_date)
        print(end_date)
    
    python_t1 = PythonOperator(
        task_id = 'python_t1',
        python_callable=python_function1,
        op_kwargs={'start_date':'{{data_interval_start | ds}}' , 'end_date' : '{{data_interval_end | ds}}'}
    )

    def python_function1_2(start_date , end_date):
        print(start_date)
        print(end_date)

    python_t1_2 = PythonOperator(
        task_id = 'python_t1_2',
        python_callable=python_function1_2,
        op_args=['{{data_interval_start | ds}}' , '{{data_interval_end | ds}}']
    )

    @task(task_id='python_t2')
    def python_function2(**kwargs):
        print(kwargs)
        print('ds:' + kwargs['ds'])
        print('ts:' + kwargs.get('ts')) #kwargs['ds'] 와 동일 
        print('data_interval_start:' + str(kwargs.get('data_interval_start')))
        print('data_interval_end:' + str(kwargs.get('data_interval_end')))
        print('task_instance' + str(kwargs.get('ti')))

    python_t1 >> python_t1_2 >> python_function2()
    #앞에 두개는 같은 결과를 가지고 오게 됨.