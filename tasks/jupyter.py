"""This module contains a set of helpfull Invoke Tasks for working with Jupyter"""
from invoke import task


@task
def notebook(
    context,
):
    """Run jupyter notebook"""
    context.run("jupyter notebook")
