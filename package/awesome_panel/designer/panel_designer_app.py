import datetime
import importlib
import pathlib
import sys
import traceback

import panel as pn
import param

from awesome_panel.application import assets

DESIGN_PARAMETERS = [
    "background",
    "height",
    "sizing_mode",
    "style",
    "width",
]

ACTION_PARAMETERS = [
    "reload_component_instance",
    "reload_css_file",
    "reload_js_file",
    "stop_server",
]

ACTION_WIDGETS = {
    "reload_component_instance": {"button_type": "success"},
    "stop_server": {"button_type": "danger"},
}

CSS = """
body {
    margin: 0px;
    max-width: 100vw;
    min-height: 100vh;
    margin: 0px;
}

.bk.designer-design-pane .markdown a {
    color: black;
    font-style: normal;
    text-decoration: none;
}

.bk-root .bk-btn-primary, .bk-root .bk-btn-primary:hover, .bk-root .bk-btn-primary.bk-active {
    background: #66bb6a;
    border-color: #66bb6a;
}

.bk.designer-design-pane {
    color: black;
    border-left-color: #9E9E9E;
    border-left-width: 1px;
    border-left-style: solid;
    border-bottom-color: #9E9E9E;
    border-bottom-width: 1px;
    border-bottom-style: solid;
}"""

class EmptyComponent(param.Parameterized):
    view = param.ClassSelector(class_=pn.Column)
    def __init__(self, **params):
        super().__init__(**params)

        view = pn.Column("# Empty Component")

class StoppedComponent(param.Parameterized):
    view = param.ClassSelector(class_=pn.Column)
    def __init__(self, **params):
        super().__init__(**params)

        self.view = pn.Column("# Stopped")

class PanelDesignerApp(param.Parameterized):
    title = param.String("Awesome Panel Designer", allow_None=False)
    logo_url = param.String(assets.SPINNER_PANEL_STATIC_LIGHT, allow_None=False)
    design_parameters = param.List(DESIGN_PARAMETERS)

    css_path = param.Parameter(constant=True)
    js_path = param.Parameter(constant=True)

    component = param.Parameter(constant=True)
    component_parameters = param.Dict()
    component_instance = param.Parameter()

    modules_to_reload = param.List()

    sub_component_instance = param.ObjectSelector()

    reload_component_instance = param.Action(label="RELOAD COMPONENT")
    reload_css_file = param.Action(label="RELOAD CSS")
    reload_js_file = param.Action(label="RELOAD JS")
    show = param.Action(label="SHOW")
    stop_server = param.Action(label="STOP SERVER AND EXIT")

    view = param.ClassSelector(class_=pn.Column, constant=True)

    logo_pane = param.ClassSelector(class_=pn.pane.HTML, constant=True)
    title_pane = param.ClassSelector(class_=pn.pane.Markdown, constant=True)
    design_pane = param.ClassSelector(class_=pn.WidgetBox, constant=True)
    action_pane = param.ClassSelector(class_=pn.Param, constant=True)
    settings_pane = param.ClassSelector(class_=pn.Param, constant=True)

    component_pane = param.ClassSelector(class_=pn.Column, constant=True)

    css_pane = param.ClassSelector(class_=pn.pane.HTML, constant=True)
    js_pane = param.ClassSelector(class_=pn.pane.HTML, constant=True)

    error_pane = param.ClassSelector(class_=pn.pane.Markdown, constant=True)


    server = param.Parameter(constant=True)
    last_reload = param.String(constant=True)

    def __init__(self, **params):
        if not "name" in params:
            params["name"]="Awesome Panel Designers App"
        if not "component_parameters" in params or params["component_parameters"] is None:
            params["component_parameters"] = {}

        if "logo_pane" not in params:
            params["logo_pane"] = pn.pane.HTML(name="Logo Pane",
                sizing_mode="fixed", width=70, height=70, align="center"
            )
        if "title_pane" not in params:
            params["title_pane"] = pn.pane.Markdown(sizing_mode="fixed", width=255, align="center", margin=(15,5,0,30), css_classes=["designer-title-pane"])
        if "css_pane" not in params:
            params["css_pane"] = pn.pane.HTML(name="CSS Pane", sizing_mode="fixed", width=0, height=0, margin=0, css_classes=["designer-css-pane"])
        if "js_pane" not in params:
            params["js_pane"] = pn.pane.HTML(name="JS Pane", sizing_mode="fixed", width=0, height=0, margin=0, css_classes=["designer-js-pane"])
        if "component_pane" not in params:
            params["component_pane"] = pn.Column(name="Component Pane",
                sizing_mode="stretch_both", css_classes=["designer-component-pane"]
            )
        if "design_pane" not in params:
            params["design_pane"] = pn.WidgetBox(
                sizing_mode="stretch_height", width=410, background="#F5F5F5", margin=(0,0,0,0), css_classes=["designer-design-pane"]
            )
        if "action_pane" not in params:
            params["action_pane"] = pn.Param(
                self,
                sizing_mode="stretch_width",
                parameters=ACTION_PARAMETERS,
                widgets=ACTION_WIDGETS,
                show_name=False,
                css_classes=["designer-action-pane"]
            )
        if "settings_pane" not in params:
            params["settings_pane"] = pn.Param(sizing_mode="stretch_both", css_classes=["designer-settings-pane"])
        if "error_pane" not in params:
            params["error_pane"] = pn.pane.Markdown(sizing_mode="stretch_both", css_classes=["designer-error-pane"])
        if "view" not in params:
            params["view"] = pn.Column(sizing_mode="stretch_both", margin=(0,0,0,0), name="Panel Designer View", css_classes=["designer-view"])

        super().__init__(**params)

        self.logo_pane.object = f"<a href='https://panel.holoviz.org' target='_blank'><img src='{self.logo_url}' style='height:100%'></img></a>"
        self.design_pane[:] = [
            pn.Row(
                self.title_pane,
                self.logo_pane,
                sizing_mode="stretch_width",
                margin=0,
            ),
            pn.layout.Divider(margin=(20,10,10,10)),
            self.action_pane,
            self.param.last_reload,
            pn.layout.Divider(margin=(20,10,10,10)),
            self.settings_pane,
            self.css_pane,
            self.js_pane,
            pn.pane.HTML('<link href="https://fonts.googleapis.com/css?family=Roboto:300,400,500&display=swap" rel="stylesheet">')
        ]

        self.view[:] = [
            pn.Row(self.component_pane, self.design_pane, sizing_mode="stretch_both"),
        ]

        self.reload_component_instance = self._reload_component_instance
        self.reload_css_file = self._reload_css_file
        self.reload_js_file = self._reload_js_file
        self.show = self._show
        self.stop_server = self._stop_server

        self._update_title_pane()

        self.reload_component_instance()
        self.reload_css_file()
        self.reload_js_file()

    def _reload_component_instance(self, _=None):
        print("reload start", self.name, datetime.datetime.now())
        try:
            if not self.component:
                with param.edit_constant(self):
                    self.component = EmptyComponent

            if not self.component_instance:
                self.component_instance = self.component(**self.component_parameters)
            else:
                self._reload_component()
                self.component_instance = self.component(**self.component_parameters)

            if hasattr(self.component_instance, "view"):
                self.component_pane[:] = [self.component_instance.view, pn.Spacer()]
                self.settings_pane.object = self.component_instance
            else:
                raise NotImplementedError
        except Exception as ex:
            breakpoint()
            self.error_pane.object = "# Error " + traceback.format_exc()
            self.component_pane[:] = [self.error_pane, pn.Spacer()]

        self._update_last_reload()
        print("reload end", self.name, datetime.datetime.now())

    def _update_last_reload(self):
        with param.edit_constant(self):
            self.last_reload = str(datetime.datetime.now())

    def _reload_component(self):
        for mod in self.modules_to_reload:
            importlib.reload(mod)

        mod = sys.modules[self.component.__module__]
        importlib.reload(mod)
        with param.edit_constant(self):
            self.component = getattr(mod, self.component.__name__)

    def _reload_css_file(self, _=None):
        if not self.css_path:
            pass
        elif isinstance(self.css_path, pathlib.Path):
            self.css_pane.object = "<style>" + self.css_path.read_text() + "</style>"
        else:
            raise NotImplementedError
        self._update_last_reload()

    def _reload_js_file(self, _=None):
        if not self.js_path:
            pass
        elif isinstance(self.js_path, pathlib.Path):
            self.js_pane.object = "<script>" + self.js_path.read_text() + "</script>"
        else:
            raise NotImplementedError
        self._update_last_reload()

    def _show(self, _=None):
        if not self.server:
            with param.edit_constant(self):
                self.server = self.view.show()
        else:
            raise NotImplementedError

    def _stop_server(self, _=None):
        self.view[:] = [StoppedComponent().view]
        if self.server:
            self.server.stop()
            with param.edit_constant(self):
                self.server = None
        raise SystemExit

    @param.depends("component_instance", watch=True)
    def _update_sub_component_instance(self):
        self.param.sub_component_instance.default = self.component_instance
        self.sub_component_instance = self.component_instance

    def __repr__(self):
        return f"PanelDesigner(self.__name__)"

    def __str__(self):
        return f"PanelDesigner(self.__name__)"

    @param.depends("title", watch=True)
    def _update_title_pane(self):
        self.title_pane.object = f"""\
# [Panel Designer](https://panel.holoviz.org)

By **[awesome-panel.org](https://awesome-panel.org)**"""
