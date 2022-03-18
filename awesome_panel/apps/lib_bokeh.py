"""
The purpose of this app is to demonstrate that Panel works with the tools you know and love
&#10084;&#65039;, including Bokeh. It supports both light and dark theme.
"""
import numpy as np
import panel as pn
from bokeh.plotting import figure
from scipy.integrate import odeint

from awesome_panel import config

config.extension(url="lib_bokeh")


def get_plot():
    """Returns a Bokeh plot"""
    # pylint: disable=invalid-name
    sigma = 10
    rho = 28
    beta = 8.0 / 3
    theta = 3 * np.pi / 4

    def lorenz(xyz, t): # pylint: disable=unused-argument
        x, y, z = xyz
        x_dot = sigma * (y - x)
        y_dot = x * rho - x * z - y
        z_dot = x * y - beta * z
        return [x_dot, y_dot, z_dot]

    initial = (-10, -7, 35)
    t = np.arange(0, 100, 0.006)

    solution = odeint(lorenz, initial, t)

    x = solution[:, 0]
    y = solution[:, 1]
    z = solution[:, 2]
    xprime = np.cos(theta) * x - np.sin(theta) * y

    colors = [
        "#C6DBEF",
        "#9ECAE1",
        "#6BAED6",
        "#4292C6",
        "#2171B5",
        "#08519C",
        "#08306B",
    ]

    plot = figure(title="Lorenz attractor example", tools=["pan,wheel_zoom,box_zoom,reset,hover"])

    plot.multi_line(
        np.array_split(xprime, 7),
        np.array_split(z, 7),
        line_color=colors,
        line_alpha=0.8,
        line_width=1.5,
    )
    return plot


PLOT = get_plot()
pn.pane.Bokeh(PLOT, height=700, sizing_mode="stretch_both").servable()
