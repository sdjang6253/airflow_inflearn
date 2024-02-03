from airflow.models.dag import DAG
from operators.seoul_api_to_csb_operator import SeoulApiToCsvOperator
import pendulum

with DAG(
    dag_id="dags_seoul_api_corona",
    schedule='0 7 * * *',
    start_date=pendulum.datetime(2024, 1, 1, tz="Asia/Seoul"),
    catchup=False,
) as dag:
    
    '''서울시 코로나 19 확진자 발생 동향'''
    tb_corona19_count_status = SeoulApiToCsvOperator(
        task_id='tb_corona19_count_status',
        dataset_nm='TbCorona19CountStatus',
        path='/opt/airflow/files/TbCorona19CountStatus/{{data.interval_end.in_timezone("Asia/Seoul") | ds_nodash}}', 
        file_name='TbCorona19CountStatus.csv'
    )
    '''
       여기서 path 의 위치가 /opt/airflow/files 로 시작하는 이유
       결국 이 task 를 수행하는 곳은 Worker Container 이기 때문에 이렇게 지정
       현재 /opt/airflow/files 는 WSL 디렉토리와 연결이 되어 있지 않기 때문에 , container 가 내렸다 올라갈 때 마다 container 데이터는 사라지고 있음
       즉 files  를 docker-compose.yml 에 volumes 에 추가해 주어야 합니다. 
    '''
    '''서울시 코로나 19 확진자 발생 동향'''
    tv_corona19_vaccine_stat_new = SeoulApiToCsvOperator(
        task_id='tv_corona19_vaccine_stat_new',
        dataset_nm='tvCorona19VaccinestatNew',
        path='/opt/airflow/files/tvCorona19VaccinestatNew/{{data.interval_end.in_timezone("Asia/Seoul") | ds_nodash}}',
        file_name='tvCorona19VaccinestatNew.csv'
    )
    
    tb_corona19_count_status >> tv_corona19_vaccine_stat_new
    