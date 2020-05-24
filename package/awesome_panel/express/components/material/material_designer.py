"""In this module we configure the Awesome Panel Designer for Material Components

This is used for development and manual testing
"""
import panel as pn

from awesome_panel.designer import Designer, ReloadService
from awesome_panel.express.components import material


def view() -> pn.Column:
    """The Designer with the Material Components

    Returns:
        pn.Column: A Column with the Designer and the Material Components
    """
    button_service = ReloadService(
        component=material.MWCButton, component_parameters={"name": "Click Me"}
    )
    select_service = ReloadService(
        component=material.MWCSelect,
        component_parameters={"name": "Select Me", "options": {"a": "aaa", "b": "bbb", "c": "ccc"}},
    )

    reload_services = [select_service, button_service]
    designer = Designer(reload_services=reload_services)
    pn.config.js_files["mwc"] = material.MWC_JS

    return pn.Column(designer.view, material.fonts_pane, sizing_mode="stretch_both",)


if __name__.startswith("__main__"):
    view().show()
