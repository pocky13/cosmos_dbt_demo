from datetime import datetime

from cosmos import DbtTaskGroup, RenderConfig, TestBehavior
from config import profile_config, project_config

from airflow.decorators import dag
from airflow.operators.empty import EmptyOperator


@dag(
    description="This DAG runs dbt with a selected model.",
    schedule_interval=None,
    start_date=datetime(2023, 1, 1),
    catchup=False,
)
def selected_dag() -> None:
    pre_dbt = EmptyOperator(task_id="pre_dbt")
    jaffle_shop = DbtTaskGroup(
        group_id="selected_dag",
        project_config=project_config,
        profile_config=profile_config,
        render_config=RenderConfig(
            select=["+orders"],
            test_behavior=TestBehavior.NONE,
        ),
    )
    post_dbt = EmptyOperator(task_id="post_dbt")

    pre_dbt >> jaffle_shop >> post_dbt


selected_dag()
