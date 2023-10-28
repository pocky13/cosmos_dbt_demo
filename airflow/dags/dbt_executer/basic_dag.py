from datetime import datetime

from cosmos import DbtTaskGroup
from config import profile_config, project_config

from airflow.decorators import dag
from airflow.operators.empty import EmptyOperator


@dag(
    description="run all models in dbt project",
    schedule_interval=None,
    start_date=datetime(2023, 1, 1),
    catchup=False,
)
def basic_dag() -> None:
    pre_dbt = EmptyOperator(task_id="pre_dbt")
    jaffle_shop = DbtTaskGroup(
        group_id="basic_dag",
        project_config=project_config,
        profile_config=profile_config,
    )
    post_dbt = EmptyOperator(task_id="post_dbt")

    pre_dbt >> jaffle_shop >> post_dbt


basic_dag()
