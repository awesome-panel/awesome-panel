"""This module contains a set of helpfull Invoke Tasks for working with Panel"""
from invoke import task, Context


@task
def bootstrap_dashboard(context, dev=False):
    """Starts the Panel Server and serves the Bootstrap Dashboard App

    Arguments:
        context {Context} -- The Invoke Context object


    Keyword Arguments:
        dev {bool} -- Whether or not to run in Debug Mode with autoreload (default: {False})
    """
    if dev:
        command = "python -m panel serve gallery/bootstrap_dashboard --dev --show"
    else:
        command = "panel serve bootstrap_dashboard"

    context.run(command)
