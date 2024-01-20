Jinja Template 을 사용한다. 
{{}} 안에 입력을 하면 해당 변수가 템플릿으로 입력이 된다. 
주로 사용하는 tempalte 

link (https://airflow.apache.org/docs/apache-airflow/stable/templates-ref.html)
{{ data_interval_start }}
{{ data_interval_end }}
{{ ds }}
ds 는 data_interval_start 랑 같으나, 타입이 DateTime 이 아닌 str 이다.

Operator 에도 적용 가능하고, 
link (https://airflow.apache.org/docs/apache-airflow/stable/_api/airflow/operators/bash/index.html#airflow.operators.bash.BashOperator)
안에 보면 Parameter 가 있는데, bash_command ~~~ (templated) 처럼 끝에 templated 가 있으 곳에만 적용이 가능하다. 
+ 하단에 templated_field 라는곳에도 있음. 

Python Operator 같은 경우에는
templated_fileds 에는 templates_dict , op_args , op_kwargs 총 세개를 가지고 있게 된다고 적혀있음, 
따라서 Parameters 탭에는 적혀있지 않지만 실제로는 템플릿 사용 가능. 
