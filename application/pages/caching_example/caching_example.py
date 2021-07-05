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

import holoviews as hv
import hvplot.pandas  # pylint: disable=unused-import
import numpy as np
import pandas as pd
import panel as pn
from diskcache import FanoutCache
from panel.template import FastListTemplate

from awesome_panel_extensions.site import site

hv.extension("bokeh")


cache = FanoutCache(".cache", name="all")

APPLICATION = site.create_application(
    url="caching-example",
    name="Caching Example",
    author="Marc Skov Madsen",
    description="""An app demonstrating how to speed up your app using caching.""",
    description_long=__doc__,
    thumbnail="https://raw.githubusercontent.com/MarcSkovMadsen/awesome-panel/master/assets/images/thumbnails/caching-example.png",
    resources = {
        "code": "https://github.com/MarcSkovMadsen/awesome-panel/tree/master/application/pages/caching_example/caching_example.py",
        "mp4": "https://raw.githubusercontent.com/MarcSkovMadsen/awesome-panel-assets/master/awesome-panel/applications/caching-example.mp4",
    },
    tags=["Panel", "Caching"],
)

ACCENT_COLOR = "#C01754"

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


@site.add(APPLICATION)
def view() -> FastListTemplate:  # pylint: disable=too-many-locals
    """Returns the Caching Example app

    Returns:
        FastListTemplate: The Caching Example app is layed out using the FastListTemplate
    """
    pn.config.sizing_mode = "stretch_width"
    template = FastListTemplate(site="Awesome Panel", title="Caching Example")

    # Create Cached Functions
    # We seperate the case of different users such that one user cannot clear or preload the
    # cache of another user
    session_id = str(uuid.uuid4())

    @cache.memoize(name="load" + session_id, expire=CACHE_EXPIRY)
    def _load_data_cached(frac=0.1):
        return _load_data(frac=frac)

    @cache.memoize(name="plot" + session_id, expire=CACHE_EXPIRY)
    def _plot_data_cached(frac):
        return _plot_data(frac)

    # Create Widgets
    frac = pn.widgets.FloatSlider(value=0.1, start=0.1, end=1.0, step=0.1, name="Fraction of data")
    duration = pn.widgets.StaticText(value="", name="Duration")
    use_cache = pn.widgets.Checkbox(value=False, name="Use Cache")
    preload_cache = pn.widgets.Button(name="Preload Cache", button_type="primary", disabled=True)
    clear_cache = pn.widgets.Button(name="Clear Cache", disabled=True)
    plot_panel = pn.pane.HoloViews(min_height=500, sizing_mode="stretch_both")
    preload_progress = pn.widgets.Progress(
        name="Progress", active=False, value=0, max=100, sizing_mode="stretch_width", disabled=True
    )

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

    @pn.depends(frac=frac, watch=True)
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
    def _update_cache_widgets(use_cache):
        disabled = not use_cache
        preload_cache.disabled = disabled
        clear_cache.disabled = disabled
        preload_progress.disabled = disabled

    # Layout the app
    intro_section = APPLICATION.intro_section()
    analytics_app_section = pn.Column(
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
        frac,
        duration,
        use_cache,
        plot_panel,
        clear_cache,
        preload_cache,
        preload_progress,
    )

    template.main[:] = [
        intro_section,
        analytics_app_section,
    ]

    pn.state.onload(lambda: frac.param.trigger("value"))

    return template


if __name__.startswith("bokeh"):
    view().servable()
