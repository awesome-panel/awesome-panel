"""In this module we provide functionality to develop a Material Design template
using primarely the Material Web Components"""
from typing import List

VERSION = "0.14.1"
MWC_COMPONENTS = [
    "mwc-button>"
    # "mwc-bottom-app-bar>"
    # "mwc-card>"
    "mwc-checkbox>"
    # "mwc-chip>"
    # "mwc-circular-progress>"
    # "mwc-data-table>"
    "mwc-dialog>"
    "mwc-drawer>"
    "mwc-fab>"
    "mwc-formfield>"
    "mwc-icon-button-toggle>"
    "mwc-icon-button>"
    "mwc-icon>"
    "mwc-linear-progress>"
    "mwc-list>"
    "mwc-menu>"
    "mwc-radio>"
    "mwc-select>"
    "mwc-slider>"
    "mwc-snackbar>"
    "mwc-switch>"
    "mwc-tab-bar>"
    "mwc-tab>"
    "mwc-textarea>"
    "mwc-textfield>"
    "mwc-top-app-bar-fixed>"
    "mwc-top-app-bar>"
]
MWC_FONT_SCRIPTS = (
    '<link href="https://fonts.googleapis.com/css?family=Roboto:300,400,500" rel="stylesheet">'
    '<link href="https://fonts.googleapis.com/css?family=Material+Icons&display=block" rel="stylesheet">'
)


def get_component_script(component: str, version=VERSION) -> str:
    return (
        '<script type="module" src="https://unpkg.com/@material/'
        f'{component}@{version}/{component}.js?module"></script>'
    )


def get_scripts(components: List[str], version: str = VERSION, include_fonts: bool = True):
    component_script_list = [get_component_script(component, version) for component in components]
    scripts = "".join(component_script_list)
    if include_fonts:
        scripts += MWC_FONT_SCRIPTS
    return scripts
