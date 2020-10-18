import pandas as pd
import panel as pn
import param


class Something(param.Parameterized):
    str1 = param.String("1")
    str2 = param.String("2")
    dataframe = param.DataFrame()

    view = param.Parameter()

    def __init__(self, **params):
        super().__init__(**params)

        self.view = self._create_view()

    def _create_view(self):
        panel_left = pn.Param(
            self,
                parameters=["str1", "str2"],
                widgets={"str1": {"margin": (100, 100, 100, 100)}, "str2": {"background": "lightgray"}},
            )
        panel_right = pn.pane.DataFrame(
            object=self.dataframe,
            margin=(100, 0, 0, 0),
            width=200,
            height=300,
            )
        return pn.Column(
            pn.Row(
                panel_left, panel_right
            )
        )

dataframe=pd.DataFrame({"x": [1,2,3], "y": [2,4,6]})
Something(dataframe=dataframe).view.servable()
