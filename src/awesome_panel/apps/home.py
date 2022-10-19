"""## The Home Page of awesome-panel.org"""
# pylint: disable=wrong-import-position, ungrouped-imports, wrong-import-order
from panel.pane import Markdown

from awesome_panel import config
from awesome_panel.assets.markdown import HOME_TEXT

# pylint: enable=wrong-import-position, ungrouped-imports, wrong-import-order


def _add_sections():
    sections = HOME_TEXT.split("##")
    Markdown(sections[0]).servable()

    for index in range(1, len(sections)):
        Markdown("#" + sections[index], sizing_mode="stretch_width").servable()


if __name__.startswith("bokeh"):
    config.extension(url="home", main_max_width="900px", intro_section=False)

    _add_sections()
