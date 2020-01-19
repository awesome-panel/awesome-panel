import pandas as pd
import panel as pn
import param
from bokeh.models.widgets.tables import NumberFormatter


class BasePage(param.Parameterized):
    """A view of the basic functionality of Ticker.

    The user can select an endpoint and the help text, code and result will be presented."""

    frequency = param.ObjectSelector(default="q", objects={"Annual": "a", "Quarterly": "q",},)

    @param.depends("frequency")
    def _data(self,):
        # data is simple example. In the real world in would depend on among other self.frequency
        data = pd.DataFrame({"int": [1, 2, 3000,]}, index=[1, 2, 3,],)
        formatters = {"int": NumberFormatter(format="0.0", text_align="right",)}
        return pn.widgets.DataFrame(data, formatters=formatters,)

    def view(self,):
        return pn.Column(self.param, self._data,)


BasePage().view().servable()
