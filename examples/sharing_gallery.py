"""The project gallery makes it possible to view or edit a project"""
from panel_sharing.components import create_project_gallery

if __name__.startswith("bokeh"):
    create_project_gallery().servable()