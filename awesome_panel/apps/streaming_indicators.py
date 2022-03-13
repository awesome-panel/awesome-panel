"""This example shows a streaming dashboard with Panel.

Panel runs on top of the Tornado server. Tornado is a fast, asynchronous web server built to
support streaming use cases.

In panel it's very easy to support periodic updates. Here it's done via
`pn.state.add_periodic_callback(_create_callback(indicator), period=1000, count=200)`

This Dashboard is work in progress. I would like to add some different types of stats cards
including some with splines/ plots. I would also like to add some icons to make it look nice.
"""
from typing import List, Tuple

import numpy as np
import panel as pn

from awesome_panel import config

STYLE = """
.pn-stats-card div {
  line-height: 1em;
}
"""

ACCENT = config.ACCENT
OK_COLOR = config.PALETTE[2]
ERROR_COLOR = config.PALETTE[3]

SIDEBAR_FOOTER = config.menu_fast_html(app_html=config.app_menu_fast_html, accent=ACCENT)

if not STYLE in pn.config.raw_css:
    pn.config.raw_css.append(STYLE)


def _increment(value):
    draw = np.random.normal(1, 0.1, 1)[0]
    value *= draw
    value = max(0, value)
    value = min(100, value)
    return int(value)


def _create_callback(card):
    def update_card():
        card.value = _increment(card.value)

    return update_card


def create_app(intro_section, sidebar_footer) -> pn.template.FastGridTemplate:
    """Returns an app"""
    template = pn.template.FastGridTemplate(
        title="Streaming Indicators",
        row_height=140,
        accent_base_color=ACCENT,
        header_background=ACCENT,
        prevent_collision=True,
        save_layout=True,
        sidebar_footer=sidebar_footer,
    )
    template.main[0:3, :] = intro_section

    for row in range(0, 3):
        for col in range(0, 6):
            colors: List[Tuple[float, str]] = [(66, OK_COLOR), (100, ERROR_COLOR)]
            title = "Sensor " + str(row * 6 + col + 1)
            indicator = pn.indicators.Number(
                name=title,
                value=65,
                format="{value}%",
                colors=colors,
                css_classes=["pn-stats-card"],
            )
            template.main[row + 3, 2 * col : 2 * col + 2] = indicator

            pn.state.add_periodic_callback(_create_callback(indicator), period=1000, count=200)

    for row in range(3, 5):
        for col in range(0, 3):
            title = "Sensor " + str(3 * row + col + 10)
            colors = [(0.7, OK_COLOR), (1, ERROR_COLOR)]
            indicator = pn.indicators.Gauge(
                name=title, value=65, bounds=(0, 100), colors=colors, align="center"
            )
            template.main[2 * row : 2 * row + 2, 4 * col : 4 * col + 4] = pn.Row(
                pn.layout.HSpacer(),
                indicator,
                pn.layout.HSpacer(),
            )

            pn.state.add_periodic_callback(_create_callback(indicator), period=1000, count=200)

    return template


def serve():
    """Serves the app"""
    app = config.extension(url="streaming_indicators", template=None, intro_section=None)
    intro_section = app.intro_section()
    create_app(intro_section, SIDEBAR_FOOTER).servable()


if __name__.startswith("bokeh"):
    serve()
