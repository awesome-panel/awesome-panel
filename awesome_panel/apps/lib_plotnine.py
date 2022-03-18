"""
The purpose of this app is to demonstrate that Panel works with the tools you know and love
&#10084;&#65039;, including Plotnine. It supports both light and dark theme.
"""
import matplotlib.pyplot as plt
import panel as pn
from plotnine import aes, element_rect, facet_wrap, geom_point, ggplot, stat_smooth, themes
from plotnine.data import mtcars

from awesome_panel import config

config.extension(url="lib_plotnine")

THEME = config.get_theme()

def get_plot(theme="default"):
    """Returns a Plotnine Figure"""
    plt.style.use("default")
    if theme == "dark":
        plotnine_theme = themes.theme_dark() + themes.theme(
            plot_background=element_rect(fill="black", alpha=0)
        )
    else:
        plotnine_theme = themes.theme_xkcd()

    plot = (
        (
            ggplot(mtcars, aes("wt", "mpg", color="factor(gear)"))
            + geom_point()
            + stat_smooth(method="lm")
            + facet_wrap("~gear")
        )
        + plotnine_theme
        + themes.theme(figure_size=(16, 8))
    )
    return plot.draw()


PLOT = get_plot(theme=THEME)

pn.pane.Matplotlib(PLOT, height=700, sizing_mode="stretch_both").servable()
