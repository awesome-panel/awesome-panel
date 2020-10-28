"""The SiteSettings contains a collecation of user definable settings"""
import panel as pn
import param


class SiteSettings(param.Parameterized):
    """Collection of user definable settings"""

    toggle_theme = param.Action(label="Light/ Dark")
    theme = param.ObjectSelector("default", objects=["default", "dark"])
    template = param.ObjectSelector(
        "material", objects=["bootstrap", "golden", "material", "react", "vanilla"]
    )

    js_panel = param.Parameter()

    def __init__(self, **params):
        self._update_param_from_session_args("theme", params)
        self._update_param_from_session_args("template", params)

        super().__init__(**params)

        self.toggle_theme = self._toggle_theme

        if not self.js_panel:
            self.js_panel = pn.pane.HTML(height=0, width=0, margin=0, sizing_mode="fixed")

        pn.state.onload(self._configure_watchers)

    def _update_param_from_session_args(self, parameter, params):
        if parameter in pn.state.session_args:
            value = pn.state.session_args[parameter][0].decode("utf-8")
            value=value.strip("'").strip('"')
            if value in self.param[parameter].objects:
                params[parameter] = value

    def _configure_watchers(self, *_):
        if pn.state.location:
            pn.state.location.sync(self, {"theme": "theme", "template": "template"})
            self.param.watch(self._change_query_params, ["template", "theme"])

    def _toggle_theme(self, *_):
        if self.theme == "default":
            self.theme = "dark"
        else:
            self.theme = "default"

    def _change_query_params(self, *_):
        pn.state.location.unsync(self, ["theme", "template"])
        self.js_panel.object = "<script>location.reload()</script>"
