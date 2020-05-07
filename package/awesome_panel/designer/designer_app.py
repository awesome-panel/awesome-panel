import param
import panel as pn
import importlib
import sys


class DesignerApp(param.Parameterized):
    modules_to_reload = param.List()
    get_component_view = param.Action()

    view = param.ClassSelector(class_=pn.Column)

    _reload_component_action = param.Action(label="RELOAD COMPONENT")

    def __init__(self, **params):
        params["_reload_component_action"] = self._reload_component
        params["view"] = pn.Column(sizing_mode="stretch_both")
        super().__init__(**params)

        self._update_view()

    def _update_view(self):
        title_pane = pn.pane.Markdown("# Awesome Panel Designer", margin=(10, 20, 5, 25), sizing_mode="fixed", width=320)
        topbar = pn.Row(
            title_pane,
            pn.Param(
                self,
                parameters=["_reload_component_action"],
                widgets={"_reload_component_action": {"button_type": "primary"}},
                sizing_mode="fixed",
                width=300,
                show_labels=False,
                show_name=False,
                margin=(15, 5, 10, 5),
            ),
            pn.layout.HSpacer(),
            pn.Param(title_pane, parameters=["width"]),
            sizing_mode="stretch_width",
        )

        if self.get_component_view:
            component_view = self.get_component_view()
        else:
            component_view = "Not Available"

        self.view[:] = [
            topbar,
            pn.layout.Divider(),
            component_view,
        ]

    def _reload_component(self, _):
        for mod in self.modules_to_reload:
            importlib.reload(mod)
        if self.get_component_view:
            mod = sys.modules[self.get_component_view.__module__]
            importlib.reload(mod)
            self.get_component_view = getattr(mod, self.get_component_view.__name__)

        self._update_view()
