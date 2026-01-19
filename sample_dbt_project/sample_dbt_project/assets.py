from dagster import AssetExecutionContext
from dagster_dbt import DbtCliResource, dbt_assets

from .project import sample_dbt_project_project


@dbt_assets(manifest=sample_dbt_project_project.manifest_path)
def sample_dbt_project_dbt_assets(context: AssetExecutionContext, dbt: DbtCliResource):
    yield from dbt.cli(["build"], context=context).stream()
    

