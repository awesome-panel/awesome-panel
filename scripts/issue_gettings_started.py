"""Answer to [Discourse Question]\
(https://discourse.holoviz.org/t/handling-returns-from-button-on-click/733)"""
import pandas as pd
import panel as pn
import param


class MyDataframeExtractorApp(param.Parameterized):
    """Enables a user to extract and view a DataFrame"""

    data = param.DataFrame(precedence=2)
    extract = param.Action(label="Get data", precedence=1)
    view = param.Parameter()

    def __init__(self, **params):
        params["data"] = pd.DataFrame()
        params["extract"] = self._extract

        params["view"] = self._get_view()

        super().__init__(**params)

    def _extract(self, event=None):
        # self.data = pd.read_csv('mydata.csv')
        if self.data.empty:
            self.data = pd.DataFrame({"x": [1, 2, 3], "y": [2, 4, 6]})
        else:
            data = self.data.copy(deep=True)
            data["y"] = data["y"] + 1
            self.data = data

    def _get_view(self):
        top_app_bar = pn.Row(
            pn.pane.Markdown("# Panel Data Extractor"), sizing_mode="stretch_width",
        )

        content = pn.Param(
            self,
            parameters=["extract", "data"],
            widgets={
                "extract": {"button_type": "success", "width": 150, "sizing_mode": "fixed"},
                "data": {
                    "height": 600
                },  # Needed due to https://github.com/holoviz/panel/issues/919
            },
            show_name=False,
        )

        return pn.Column(top_app_bar, content, max_width=1000, sizing_mode="stretch_width",)


# MyDataframeExtractorApp().view # In notebook
MyDataframeExtractorApp().view.servable()  # using panel serve
