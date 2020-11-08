import panel as pn
import param

pn.extension()


class Streets(param.Parameterized):
    OP = param.MultiFileSelector()

    view = param.Parameter()

    def __init__(self, **params):
        super().__init__(**params)

        self.view = self._create_view()

    def _create_view(self):
        panel_left = pn.Param(
            self,
            parameters=["OP"],
            widgets={"OP": {"widget_type": pn.widgets.FileSelector, "path": "G:\\"}},
        )
        print("OP = ", self.OP)
        return pn.Column(panel_left)


Streets().view.servable()
