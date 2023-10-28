from pathlib import Path

from cosmos import ProfileConfig, ProjectConfig

dbt_project_path = Path(__file__).resolve().parents[2] / "dbt_jaffle_shop"
project_config = ProjectConfig(dbt_project_path=dbt_project_path)
profile_config = ProfileConfig(
    profile_name="jaffle_shop",
    target_name="dev",
    profiles_yml_filepath=dbt_project_path / "profiles.yml",
)
