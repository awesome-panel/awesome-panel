import time

import numpy as np
import pandas as pd
import panel as pn
import param
from diskcache import FanoutCache
from datetime import timedelta
from cachetools import cached, TTLCache

pn.config.sizing_mode = "stretch_width"

EXPIRE = 5 * 60  # 5 minutes
CACHE_DIRECTORY = "cache"

cache = FanoutCache(directory=CACHE_DIRECTORY)
# cache = pn.state.cache

#restart
from cachetools import cached, TTLCache

@cached(cache=TTLCache(maxsize=1024, ttl=600))
def _get_data(value):
    value_str = str(value)
    if value_str in cache:
        return cache[value_str]
    else:
        print("loading data", value)
        time.sleep(1)

        df = pd.DataFrame(np.random.randint(0, 100, size=(10000, 4)), columns=list("ABCD"))
        cache[value_str] = df
        print("data loaded")
        return df


class MyApp(param.Parameterized):
    value = param.Integer(default=0, bounds=(0, 10))
    data = param.Integer()
    clear_cache = param.Action()

    def __init__(self, **params):
        super().__init__(**params)

        self.data_panel = pn.pane.Str()
        self.loading_spinner = pn.widgets.indicators.LoadingSpinner(
            width=25, height=25, sizing_mode="fixed"
        )
        self.clear_cache = self._clear_cache

        self.view = pn.Column(
            self.loading_spinner,
            self.param.value,
            self.data_panel,
            self.param.clear_cache,
            max_width=500,
        )

        self._update_data()

    @param.depends("value", watch=True)
    def _update_data(self):
        self.loading_spinner.value = True
        start_time = time.monotonic()
        # [_get_data(self.value) for i in range(0,100)]
        self.data_panel.object = f"Data: {_get_data(self.value)}"
        end_time = time.monotonic()
        print(end_time - start_time)
        self.loading_spinner.value = False

    def _clear_cache(self, *events):
        cache.clear()


if __name__.startswith("bokeh"):

    MyApp().view.servable()
