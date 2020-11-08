import time

import panel as pn
import param
from diskcache import FanoutCache

pn.config.sizing_mode = "stretch_width"

EXPIRE = 5 * 60  # 5 minutes
CACHE_DIRECTORY = "cache"

# cache=pn.state.cache # Simple builtin dictionary cache
cache = FanoutCache(directory=CACHE_DIRECTORY)

# server
@cache.memoize()
def _get_data(value):
    print("loading data. Input: ", value)
    time.sleep(1)
    data = value * 2
    return data


# change


class MyApp(param.Parameterized):
    value = param.Integer(default=0, bounds=(0, 10))
    data = param.Integer()

    def __init__(self, **params):
        print(__name__)
        super().__init__(**params)

        self.data_panel = pn.pane.Str()
        self.loading_spinner = pn.widgets.indicators.LoadingSpinner(
            width=25, height=25, sizing_mode="fixed"
        )

        self.view = pn.Column(
            self.loading_spinner, self.param.value, self.data_panel, max_width=500
        )

        self._update_data()

    @param.depends("value", watch=True)
    def _update_data(self):
        self.loading_spinner.value = True
        self.data_panel.object = f"Data: {_get_data(self.value)}"
        self.loading_spinner.value = False


if __name__.startswith("bokeh"):
    MyApp().view.servable()
if __name__ == "__main__":
    pn.serve({"": MyApp().view})
