"""
The purpose of this app is to demonstrate that Panel works with the tools you know and love
&#10084;&#65039;, including VTK. It supports both light and dark theme.
"""
import panel as pn
import vtk

# pylint: disable=invalid-name, import-error, no-name-in-module
from vtk.util.colors import tomato

from awesome_panel import config

# pylint: enable=invalid-name, import-error, no-name-in-module


config.extension("vtk", url="lib_vtk")

THEME = config.get_theme()


def get_plot(theme="default"):
    """Returns a VTK RenderWindow"""
    # This creates a polygonal cylinder model with eight circumferential
    # facets.
    cylinder = vtk.vtkCylinderSource()
    cylinder.SetResolution(8)

    # The mapper is responsible for pushing the geometry into the graphics
    # library. It may also do color mapping, if scalars or other
    # attributes are defined.
    cylinder_mapper = vtk.vtkPolyDataMapper()
    cylinder_mapper.SetInputConnection(cylinder.GetOutputPort())

    # The actor is a grouping mechanism: besides the geometry (mapper), it
    # also has a property, transformation matrix, and/or texture map.
    # Here we set its color and rotate it -22.5 degrees.
    cylinder_actor = vtk.vtkActor()
    cylinder_actor.SetMapper(cylinder_mapper)
    cylinder_actor.GetProperty().SetColor(tomato)
    # We must set ScalarVisibilty to 0 to use tomato Color
    cylinder_mapper.SetScalarVisibility(0)
    cylinder_actor.RotateX(30.0)
    cylinder_actor.RotateY(-45.0)

    # Create the graphics structure. The renderer renders into the render
    # window.
    render = vtk.vtkRenderer()
    render_window = vtk.vtkRenderWindow()
    render_window.AddRenderer(render)

    # Add the actors to the renderer, set the background and size
    render.AddActor(cylinder_actor)
    if theme == "dark":
        render.SetBackground(0.13, 0.13, 0.13)
    else:
        render.SetBackground(0.97, 0.97, 0.97)
    return render_window


plot = get_plot(theme=THEME)
component = pn.pane.VTK(plot, height=700, sizing_mode="stretch_both").servable()
