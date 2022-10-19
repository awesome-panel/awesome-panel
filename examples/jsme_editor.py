"""Demonstrates the basics of the JSME Editor from panel-chemistry"""
import panel as pn

# panel_chemistry needs to be imported before you run pn.extension()
from panel_chemistry.widgets import JSMEEditor

from awesome_panel import config

config.extension("jsme", url="jsme_editor")


def _create_app():
    smiles = "N[C@@H](CCC(=O)N[C@@H](CS)C(=O)NCC(=O)O)C(=O)O"
    editor = JSMEEditor(value=smiles, height=500, format="smiles").servable()

    pn.Param(
        editor,
        parameters=["value", "jme", "smiles", "mol", "mol3000", "sdf"],
        widgets={
            "value": {"type": pn.widgets.TextAreaInput, "height": 200},
            "jme": {"type": pn.widgets.TextAreaInput, "height": 200},
            "smile": {"type": pn.widgets.TextAreaInput, "height": 200},
            "mol": {"type": pn.widgets.TextAreaInput, "height": 200},
            "mol3000": {"type": pn.widgets.TextAreaInput, "height": 200},
            "sdf": {"type": pn.widgets.TextAreaInput, "height": 200},
        },
    ).servable()

    pn.Param(
        editor,
        parameters=[
            "height",
            "width",
            "sizing_mode",
            "subscriptions",
            "format",
            "options",
            "guicolor",
        ],
        widgets={
            "options": {"height": 300},
        },
    ).servable(area="sidebar")


if __name__.startswith("bokeh"):
    _create_app()
