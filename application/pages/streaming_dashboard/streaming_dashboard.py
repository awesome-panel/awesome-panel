"""This example shows a streaming dashboard with Panel.

Panel runs on top of the Tornado server. Tornado is a fast, asynchronous web server built to
support streaming use cases.

In panel it's very easy to support periodic updates. Here it's done via
`pn.state.add_periodic_callback(_create_callback(indicator), period=1000, count=200)`

This Dashboard is work in progress. I would like to add some different types of stats cards
including some with splines/ plots. I would also like to add some icons to make it look nice.
"""
import numpy as np
import panel as pn
from panel.template import FastGridTemplate

from application.config import site

STYLE = """
.pn-stats-card div {
  line-height: 1em;
}
"""
ERROR_COLOR = "#A01346"

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


APPLICATION = site.create_application(
    url="streaming-dashboard",
    name="Streaming Dashboard",
    author="Marc Skov Madsen",
    introduction="A demonstration of a Streaming Dashboard",
    description=__doc__,
    thumbnail_url="streaming-dashboard.png",
    code_url="streaming_dashboard/streaming_dashboard.py",
    mp4_url="streaming-dashboard.mp4",
    tags=["Streaming", "Dashboard", "StatsCard"],
)


@site.add(APPLICATION)
def view():
    """Returns a servable Template"""
    pn.config.sizing_mode = "stretch_width"
    template = FastGridTemplate(title="Streaming Dashboard", row_height=140)
    template.main[0:3, :] = APPLICATION.intro_section()

    OK_COLOR = "#A01346"
    for row in range(0, 3):
        for col in range(0, 6):
            colors = [(66, OK_COLOR), (100, ERROR_COLOR)]
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


if __name__.startswith("bokeh"):
    view().servable()
