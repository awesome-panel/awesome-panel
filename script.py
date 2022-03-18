import matplotlib.pyplot as plt
import numpy as np
import panel as pn
from matplotlib import cm
from matplotlib.figure import Figure

pn.extension(template="fast")


def get_theme() -> str:
    """Returns the name of the active theme"""
    template = pn.state.template
    theme = "dark" if template.theme == pn.template.DarkTheme else "default"
    return theme


def get_plot(theme="default"):
    plt.style.use("default")
    if theme == "dark":
        plt.style.use("dark_background")
    Y, X = np.mgrid[-3:3:100j, -3:3:100j]
    U = -1 - X**2 + Y
    V = 1 + X - Y**2

    fig0 = Figure(figsize=(12, 6))
    ax0 = fig0.subplots()

    strm = ax0.streamplot(X, Y, U, V, color=U, linewidth=2, cmap=cm.autumn)
    fig0.colorbar(strm.lines)
    return fig0


plot = get_plot(theme=get_theme())

pn.pane.Matplotlib(plot, height=600, sizing_mode="scale_height", align="center").servable()

pn.Column(
    pn.Spacer(),
    pn.pane.Matplotlib(plot, height=600, sizing_mode="scale_height", align="center"),
    sizing_mode="stretch_both",
).servable()
