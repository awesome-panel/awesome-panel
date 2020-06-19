import param
import panel as pn

class AppStyler(param.Parameterized):
    body_color = param.String("#000000")

    css = param.String()

    view = param.Parameter()

    def __init__(self, **params):
        super().__init__(**params)

        self.view = pn.Column(pn.Param(self, parameters=["body_color"]), pn.Param(self, parameters=["css"]))

        self._update_css()

    @param.depends("body_color", watch=True)
    def _update_css(self):
        print("updating")
        self.css = self.body_color

    @param.depends("css", watch=True)
    def _update_css_pane(self):
        pass

AppStyler().view.servable()