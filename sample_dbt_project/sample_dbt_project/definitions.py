from dagster import Definitions
from dagster_dbt import DbtCliResource
from .assets import sample_dbt_project_dbt_assets
from .project import sample_dbt_project_project
from .schedules import schedules

defs = Definitions(
    assets=[sample_dbt_project_dbt_assets],
    schedules=schedules,
    resources={
        "dbt": DbtCliResource(project_dir=sample_dbt_project_project),
    },
)

