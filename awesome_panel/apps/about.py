"""## The About Page of awesome-panel.org"""
import panel as pn

from awesome_panel import config
from awesome_panel.assets.markdown import ABOUT_TEXT

config.extension(url="about", main_max_width="900px")

pn.pane.Markdown(ABOUT_TEXT).servable()
