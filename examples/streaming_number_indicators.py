"""
Source: https://awesome-panel.org/resources/streaming_number_indicators/
"""
from asyncio import create_task, get_event_loop, sleep

import numpy as np
import panel as pn

ACCENT = "#00A170"
OK_COLOR = ACCENT
ERROR_COLOR = "#a10031"
ALERT = 80
COLORS = [(ALERT, OK_COLOR), (100, ERROR_COLOR)]
INITIAL_VALUE = ALERT - 3

N = 18  # Number of indicators

# Can be removed when https://github.com/holoviz/panel/pull/6194 is released
CSS_FIX = """
:host(.pn-loading) .pn-loading-msg,
.pn-loading .pn-loading-msg {
  color: var(--panel-on-background-color, black) !important; 
}
"""
if not CSS_FIX in pn.config.raw_css:
    pn.config.raw_css.append(CSS_FIX)


async def update_values(values):
    """Some random updating of values."""
    while True:
        # Replace with your own code.
        new_value = np.copy(values.rx.value)

        new_value += np.random.randint(5, size=N) - 2
        new_value[new_value < 0] = 0
        new_value[new_value > 99] = 99

        values.rx.value = new_value

        await sleep(1)


@pn.cache  # We use caching to share values across all sessions in a server context
def get_values():
    # We use Reactive Expressions https://param.holoviz.org/user_guide/Reactive_Expressions.html
    return pn.rx([INITIAL_VALUE] * N)


@pn.cache  # We use caching to only update values once across all sessions in a server context
def create_update_values_task():
    values = get_values()
    create_task(update_values(values))


def get_styles(value):
    if value <= ALERT:
        return {"border": f"1px solid {OK_COLOR}", "padding": "1em", "border-radius": "3px"}
    return {"border": f"1px solid {ERROR_COLOR}", "padding": "1em", "border-radius": "3px"}


def create_indicator(index, values):
    title = f"Sensor {index}"
    value = values[index]

    return pn.indicators.Number(
        name=title,
        value=value,
        format="{value}%",
        colors=COLORS,
        margin=10,
        styles=pn.rx(get_styles)(value),
        width=165,
    )


def create_component():
    values = get_values()
    indicators = tuple(create_indicator(i, values) for i in range(len(values.rx.value)))
    layout = pn.FlexBox(*indicators)
    return layout


if pn.state.served or pn.state._is_pyodide:
    pn.extension()

    if get_event_loop().is_running():
        # We can only start the stream if the event loop is running
        create_update_values_task()

    pn.template.FastListTemplate(
        site="Awesome Panel",
        site_url="https://awesome-panel.org",
        title="Streaming Number Indicators",
        accent=ACCENT,
        theme="dark",
        theme_toggle=False,
        main=[create_component()],
        main_layout=None,
    ).servable()
