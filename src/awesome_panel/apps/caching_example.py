# pylint: disable=line-too-long
"""
In computing, a *cache* is a high-speed data storage layer which stores a subset of data,
typically transient in nature, so that future requests for that data are served up faster than
is possible by accessing the data’s primary storage location.

**Caching allows you to efficiently reuse previously retrieved or computed data** to
**speed up your exploration, jobs or apps**.

Good caching solutions for Panel are summarized in the table below

|Technology           |  Performance | Persistant | Horizontal Scaling | Vertical Scaling | Expiration | Preloading | Comments                           |
|---------------------|--------------|------------|--------------------| -----------------|---------------------|------------------------------------|-|
|`panel.state.cache` | Very Fast | No | No | Yes | No | No | Simple Dict Cache |
|[DiskCache](https://pypi.org/project/diskcache/) | Very Fast | Yes | No | Yes | Yes | Yes |  Simple Persistent Cache |
|[Redis](https://redis.io/) | Very Fast | Yes | Yes | Yes | Yes | Yes | Server solution. Works well with the distributed task queue [Celery](https://docs.celeryproject.org/en/stable/index.html)  |

Note that

- *Expiration* enables caching data for a period of time for example seconds, minutes, hours or
days.
- *Preloading* of a cache can be triggered by a cronjob or event.
- If the cache is *persisted*, i.e. stored to disk or runs on a server like Redis it can enable
caching data across jobs, applications, servers and restarts.

To learn more about caching check out the [AWS Caching Overview](https://aws.amazon.com/caching/)
"""
# pylint: enable=line-too-long
import time
import uuid

import hvplot.pandas  # pylint: disable=unused-import
import numpy as np
import pandas as pd
import panel as pn
from diskcache import FanoutCache

from awesome_panel import config

config.extension(url="caching_example")

cache = FanoutCache(".cache", name="all")


ACCENT_COLOR = config.ACCENT

CACHE_EXPIRY = 60 * 60 * 24  # seconds, i.e. one Day


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


# Create Cached Functions
# We seperate the case of different users such that one user cannot clear or preload the
# cache of another user
SESSION_ID = str(uuid.uuid4())


@cache.memoize(name="load" + SESSION_ID, expire=CACHE_EXPIRY)
def _load_data_cached(frac=0.1):
    return _load_data(frac=frac)


@cache.memoize(name="plot" + SESSION_ID, expire=CACHE_EXPIRY)
def _plot_data_cached(frac):
    return _plot_data(frac)


# Create Widgets
fraction = pn.widgets.FloatSlider(value=0.1, start=0.1, end=1.0, step=0.1, name="Fraction of data")
duration = pn.widgets.StaticText(value="", name="Duration")
use_cache = pn.widgets.Checkbox(value=False, name="Use Cache")
preload_cache = pn.widgets.Button(name="Preload Cache", button_type="primary", disabled=True)
clear_cache = pn.widgets.Button(name="Clear Cache", disabled=True)
preload_progress = pn.widgets.Progress(
    name="Progress", active=False, value=0, max=100, sizing_mode="stretch_width", disabled=True
)

plot_panel = pn.pane.HoloViews(min_height=500, sizing_mode="stretch_both")

# Setup interactivity
def _clear_cache(*_):
    cache.clear()


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
        """## Analytics App with and without Caching

Below you can explore the difference caching can make. Its based on
[DiskCache](http://www.grantjenks.com/docs/diskcache/). DiskCache uses a
combination of memory and sqllight to cache data and is simple to use with your Analytics App as it
can cache your DataFrames, Models and Plots without problems. DiskCache is
discussed on [Python Bytes Episode 217]\
(https://pythonbytes.fm/episodes/show/217/use-your-cloud-ssd-for-fast-cross-process-caching).
<fast-divider></fast-divider>
"""
    ),
    fraction,
    duration,
    use_cache,
    plot_panel,
    clear_cache,
    preload_cache,
    preload_progress,
).servable()

pn.state.onload(lambda: fraction.param.trigger("value"))
