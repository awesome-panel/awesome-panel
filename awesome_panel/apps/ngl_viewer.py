"""Demonstrates the basics of the NGLViewer from panel-chemistry"""
import panel as pn
from panel_chemistry.pane import (
    NGLViewer,
)  # panel_chemistry needs to be imported before you run pn.extension()
from panel_chemistry.pane.ngl_viewer import EXTENSIONS
from awesome_panel import config

config.extension("ngl_viewer", url="ngl_viewer")


def _create_app():
    viewer = NGLViewer(
        object="1CRN", background="#F7F7F7", min_height=700, sizing_mode="stretch_both"
    ).servable()

    file_input = pn.widgets.FileInput(accept=",".join("." + s for s in EXTENSIONS[1:]))

    def filename_callback(target, event):
        target.extension = event.new.split(".")[1]

    def value_callback(target, event):
        target.object = event.new.decode("utf-8")

    file_input.link(viewer, callbacks={"value": value_callback, "filename": filename_callback})

    header = pn.widgets.StaticText(value="<b>&#128190; File Input</b>")
    pn.layout.Column(header, file_input).servable(area="sidebar")

    pn.Param(
        viewer,
        parameters=[
            "object",
            "extension",
            "representation",
            "color_scheme",
            "custom_color_scheme",
            "effect",
        ],
        name="&#9881;&#65039; Settings",
    ).servable(area="sidebar")

    pn.Param(
        viewer, parameters=["sizing_mode", "width", "height", "background"], name="&#128208; Layout"
    ).servable(area="sidebar")


if __name__.startswith("bokeh"):
    _create_app()
