"""
# Toy DAG scheduled to run on a cron schedule and an update to any of 2 upstream datasets
"""

from airflow.decorators import dag, task
from airflow.datasets import Dataset
from pendulum import datetime
from airflow.timetables.datasets import DatasetOrTimeSchedule
from airflow.timetables.trigger import CronTriggerTimetable


@dag(
    start_date=datetime(2024, 3, 1),
    schedule=DatasetOrTimeSchedule(
        timetable=CronTriggerTimetable("0 * * * *", timezone="UTC"),
        datasets=(Dataset("dataset3") | Dataset("dataset4")),
    ),  # Runs every hour and when either of the datasets are updated
    # NEW in Airflow 2.9: Schedule a DAG both on time and conditional datasets
    # Use () instead of [] to be able to use conditional dataset scheduling!
    catchup=False,
    doc_md=__doc__,
    tags=["syntax_example"],
    default_args={"retries": 3},
)
def dataset_or_time_schedule():
    @task
    def say_hello():
        print("Hello")

    say_hello()


dataset_or_time_schedule()
