"""Helper Services"""
import inspect
import pathlib
from types import ModuleType

from application.config.settings import GITHUB_BLOB_MASTER_URL

ROOT_PATH = str(pathlib.Path.cwd()).lower()


def module_to_github_url(
    module: ModuleType,
) -> str:
    """## The link to the GitHub Source File of the URL

    Arguments:
        module {ModuleType} -- A module, for example package.awesome_panel.app.services
    Raises:
        ValueError: If the file path of the module is not in the project
    Returns:
        str -- A link to the GitHub file, for example
        'https://github.com/marcskovmadsen/awesome-panel/package/awesome_panel/app/services.py'
    """
    file_absolute = inspect.getfile(module).lower()
    if not file_absolute.startswith(ROOT_PATH):
        raise ValueError("Module is not in project!")
    if ROOT_PATH == "/app":
        file_relative = file_absolute.replace(
            "/app/",
            "/",
        )
    else:
        file_relative = file_absolute.replace(ROOT_PATH, "")
    file_relative = file_relative[1:].replace(
        "\\",
        "/",
    )
    return GITHUB_BLOB_MASTER_URL + file_relative
