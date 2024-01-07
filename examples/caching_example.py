"""
# Caching Example

See https://awesome-panel.org/resources/caching_example
"""
import time

import hvplot.pandas  # pylint: disable=unused-import
import numpy as np
import pandas as pd
import panel as pn

pn.extension(design="material")

ACCENT_COLOR = "#1f77b4"

np.random.seed([3, 1415])
PERIODS = 1 * 24 * 60  # minutes. I.e. 1 days
DATA = pd.DataFrame(
    {
        "time": pd.date_range("2020-01-01", periods=PERIODS, freq="T"),
        "price": np.random.randn(PERIODS) + 98,
    }
)

def _load_data(frac=0.1):
    time.sleep(0.5 + frac * 0.5)
    return DATA.sample(frac=frac)

def _plot_data(frac=0.1):
    time.sleep(0.5)
    data = _load_data(frac)
    return data.hvplot(x="time", y="price")

@pn.cache(per_session=True, ttl=60*60*24)
def _plot_data_cached(frac):
    return _plot_data(frac)


# Create Widgets
fraction = pn.widgets.FloatSlider(value=0.1, start=0.1, end=1.0, step=0.1, name="Fraction of data")
duration = pn.widgets.StaticText(value="", name="Time to create plot")
use_cache = pn.widgets.Checkbox(value=False, name="Use Cache")
preload_cache = pn.widgets.Button(name="Preload Cache", button_type="primary", disabled=True)
clear_cache = pn.widgets.Button(name="Clear Cache", disabled=True)
preload_progress = pn.widgets.Progress(
    name="Progress", active=False, value=0, max=100, sizing_mode="stretch_width", disabled=True
)

plot_panel = pn.pane.HoloViews(min_height=500, sizing_mode="stretch_both")

# Setup interactivity
def _clear_cache(*_):
    _plot_data_cached.clear()


clear_cache.on_click(_clear_cache)


def _preload_cache(*_):
    for index in range(0, 11, 1):
        frac_ = round(index / 10, 1)
        preload_progress.value = int(frac_ * 100)
        _plot_data_cached(frac_)
    preload_progress.value = 0


preload_cache.on_click(_preload_cache)


@pn.depends(frac=fraction, watch=True)
def _update_plot(frac):
    start_counter = time.perf_counter()

    frac = round(frac, 1)
    if use_cache.value:
        plot = _plot_data_cached(frac)
    else:
        plot = _plot_data(frac)

    end_counter = time.perf_counter()
    duration.value = str(round(end_counter - start_counter, 4)) + " seconds"

    # Please note DiskCache does not cache the options
    plot.opts(color=ACCENT_COLOR, responsive=True)
    plot_panel.object = plot


@pn.depends(use_cache=use_cache, watch=True)
def _update_cache_widgets(use_cache):  # pylint: disable=redefined-outer-name
    disabled = not use_cache
    preload_cache.disabled = disabled
    clear_cache.disabled = disabled
    preload_progress.disabled = disabled


# Layout the app
pn.Column(
    pn.pane.Markdown(
        "# Speed up slow functions with caching", sizing_mode="stretch_width"
    ),
    fraction,
    duration,
    use_cache,
    plot_panel,
    pn.Row(preload_cache, clear_cache,),
    preload_progress,
).servable()

pn.state.onload(lambda: fraction.param.trigger("value"))
