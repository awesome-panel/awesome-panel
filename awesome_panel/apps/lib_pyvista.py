"""
The purpose of this app is to demonstrate that Panel works with the tools you know and love
&#10084;&#65039;, including PyVista. It supports both light and dark theme.
"""

import panel as pn
import pyvista as pv

from awesome_panel import config

config.extension("vtk", url="lib_pyvista")

THEME = config.get_theme()
ACCENT = config.ACCENT


def get_plot(theme=THEME, accent_base_color=ACCENT):
    """Returns a PyVista Plotter"""
    plotter = pv.Plotter()  # we define a pyvista plotter
    if theme == "dark":
        plotter.background_color = (0.13, 0.13, 0.13)
    else:
        plotter.background_color = (0.97, 0.97, 0.97)

    # we create a `VTK` panel around the render window
    pvcylinder = pv.Cylinder(resolution=8, direction=(0, 1, 0))
    cylinder_actor = plotter.add_mesh(pvcylinder, color=accent_base_color, smooth_shading=True)
    cylinder_actor.RotateX(30.0)
    cylinder_actor.RotateY(-45.0)
    plotter.add_mesh(
        pv.Sphere(theta_resolution=8, phi_resolution=8, center=(0.5, 0.5, 0.5)),
        color=accent_base_color,
        smooth_shading=True,
    )
    return plotter.ren_win


plot = get_plot()
pn.panel(plot, height=700, sizing_mode="stretch_both").servable()
