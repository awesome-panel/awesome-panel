"""
The purpose of this app is to demonstrate that Panel works with the tools you know and love
&#10084;&#65039;, including Matplotlib. It supports both light and dark theme.
"""
import matplotlib.pyplot as plt
import numpy as np
import panel as pn
from matplotlib import cm
from matplotlib.figure import Figure

from awesome_panel import config

config.extension(url="lib_matplotlib")


def get_plot(theme="default") -> Figure:
    """Returns a Matplotlib Figure"""
    # pylint: disable=invalid-name
    plt.style.use("default")
    if theme == "dark":
        plt.style.use("dark_background")
    Y, X = np.mgrid[-3:3:100j, -3:3:100j]  # type: ignore
    U = -1 - X**2 + Y
    V = 1 + X - Y**2

    fig0 = Figure(figsize=(12, 6))
    ax0 = fig0.subplots()

    # pylint: disable=no-member
    strm = ax0.streamplot(X, Y, U, V, color=U, linewidth=2, cmap=cm.autumn)
    fig0.colorbar(strm.lines)
    return fig0


plot = get_plot(theme=config.get_theme())

pn.Column(
    pn.pane.Matplotlib(plot, height=600, sizing_mode="scale_height", align="center"),
    pn.layout.HSpacer(height=0),
    sizing_mode="stretch_both",
).servable()
