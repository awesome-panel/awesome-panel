import panel as pn
import param

PARAMETERS = ["template"]

class SiteSettings(param.Parameterized):
    """Collection of user definable settings"""

    template = param.ObjectSelector(
        "material", objects=["bootstrap", "golden", "material", "react", "vanilla"]
    )
    changes = param.Integer(default=0)

    settings_panel = param.Parameter()
    view = param.Parameter()

    def __init__(self, **params):
        print("Init", 1)
        if "template" in pn.state.session_args:
            value=pn.state.session_args["template"][0].decode("utf8").strip("'").strip('"').replace("%22", "")
            print(value, type(value))
            params["template"]=value

        super().__init__(**params)
        print("Init", 2)

        self.js_panel = pn.pane.HTML()
        self.settings_panel = pn.Param(
            self, parameters=["template", "changes"]
        )

        self.view = pn.Row(self.settings_panel, self.js_panel)
        self.param.watch(self._reload, ["template"])

    @param.depends("template", watch=True)
    def _update_changes(self):
        self.changes+=1

    def _reload(self, *_):
        pn.state.location.update_query(template=self.template)
        self.js_panel.object = "<script>location.reload()</script>"

if __name__.startswith("bokeh"):
    SiteSettings().view.servable()