"""
This DAG shows how to create several tasks from one definition using .override 
"""

from airflow.decorators import dag, task


@dag(
    start_date=None,
    schedule=None,
    catchup=False,
    tags=["syntax_example"],
    default_args={"retries": 2},
)
def override_dag():

    @task
    def print_num(num: int):
        print(num)

    print_num(num=19)
    print_num.override(task_id="print_other_num")(num=23)
    print_num.override(task_id="print_another_num", retries=3)(num=42)


override_dag()
