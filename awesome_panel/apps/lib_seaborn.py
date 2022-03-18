"""
The purpose of this app is to demonstrate that Panel works with the tools you know and love
&#10084;&#65039;, including Seaborn. It supports both light and dark theme.
"""
import matplotlib.pyplot as plt
import panel as pn
import seaborn as sns

from awesome_panel import config

config.extension(url="lib_seaborn")

penguins = sns.load_dataset("penguins")

THEME = config.get_theme()
ACCENT = config.ACCENT


def get_plot(theme=THEME, accent_base_color=ACCENT):
    """Returns a seaborn Figure"""
    if theme == "dark":
        sns.set_style("darkgrid")
        plt.style.use("dark_background")
    else:
        plt.style.use("default")
        sns.set_style("whitegrid")

    displot = sns.displot(penguins, x="flipper_length_mm", color=accent_base_color)
    fig0 = displot.fig
    fig0.set_size_inches(16, 8)
    return fig0


plot = get_plot()
pn.pane.Matplotlib(plot, height=700, sizing_mode="stretch_both").servable()
