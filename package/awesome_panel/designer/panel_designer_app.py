import datetime
import importlib
import pathlib
import sys
import traceback

import panel as pn
import param

from awesome_panel.application import assets
from awesome_panel.designer import config
from awesome_panel.designer.components import (
    EmptyComponent,
    StoppedComponent,
    CenteredComponent,
    TitleComponent,
)


class PanelDesignerApp(param.Parameterized):
    component = param.Parameter()
    component_parameters = param.Dict()
    component_instance = param.Parameter()
    css_path = param.Parameter(constant=True)
    js_path = param.Parameter(constant=True)
    modules_to_reload = param.List()
    action_pane = param.ClassSelector(class_=pn.Column, constant=True)
    settings_pane = param.ClassSelector(class_=pn.Param, constant=True)

    reload_component_instance = param.Action(label="RELOAD COMPONENT")
    reload_css_file = param.Action(label="RELOAD CSS")
    reload_js_file = param.Action(label="RELOAD JS")
    css_pane = param.ClassSelector(class_=pn.pane.HTML, constant=True)
    js_pane = param.ClassSelector(class_=pn.pane.HTML, constant=True)
    error_pane = param.ClassSelector(class_=pn.pane.Markdown, constant=True)
    last_reload = param.String(constant=True)

    show = param.Action(label="SHOW")
    stop_server = param.Action(label="STOP SERVER AND EXIT")

    title_component = param.ClassSelector(
        class_=TitleComponent, constant=True, label="Title Component"
    )

    designer_pane = param.ClassSelector(class_=pn.WidgetBox, constant=True)
    component_pane = param.ClassSelector(class_=CenteredComponent, constant=True)
    stop_server_pane = param.ClassSelector(class_=pn.Param, constant=True)

    view = param.ClassSelector(class_=pn.Column, constant=True)

    server = param.Parameter(constant=True)


    def __init__(self, **params):
        if not "name" in params:
            params["name"] = "Awesome Panel Designers App"
        if not "component_parameters" in params or params["component_parameters"] is None:
            params["component_parameters"] = {}

        if "title_component" not in params:
            params["title_component"] = TitleComponent()
        if "css_pane" not in params:
            params["css_pane"] = pn.pane.HTML(
                name="CSS Pane",
                sizing_mode="fixed",
                width=0,
                height=0,
                margin=0,
                css_classes=["designer-css-pane"],
            )
        if "js_pane" not in params:
            params["js_pane"] = pn.pane.HTML(
                name="JS Pane",
                sizing_mode="fixed",
                width=0,
                height=0,
                margin=0,
                css_classes=["designer-js-pane"],
            )
        if "component_pane" not in params:
            params["component_pane"] = CenteredComponent(
                name="Component Pane",
                sizing_mode="stretch_both",
                css_classes=["designer-component-pane"],
            )
        if "designer_pane" not in params:
            params["designer_pane"] = pn.WidgetBox(
                sizing_mode="stretch_height",
                width=410,
                background="#F5F5F5",
                margin=(0, 0, 0, 0),
                css_classes=["designer-design-pane"],
            )
        if "action_pane" not in params:
            params["action_pane"] = pn.Column(
                pn.Param(
                    self,
                    sizing_mode="stretch_width",
                    parameters=config.ACTION_PARAMETERS,
                    widgets=config.ACTION_WIDGETS,
                    show_name=False,
                    css_classes=["designer-action-pane"],
                ),
                sizing_mode="stretch_width",
            )
        if "settings_pane" not in params:
            params["settings_pane"] = pn.Param(
                sizing_mode="stretch_both",
                css_classes=["designer-settings-pane"],
                margin=(10, 25, 10, 5),
            )
        if "error_pane" not in params:
            params["error_pane"] = pn.pane.Markdown(
                sizing_mode="stretch_both", css_classes=["designer-error-pane"]
            )
        if "stop_server_pane" not in params:
            params["stop_server_pane"] = pn.Param(
                self,
                parameters=["stop_server"],
                widgets={"stop_server": {"button_type": "danger"}},
                sizing_mode="stretch_width",
                show_name=False,
            )
        if "view" not in params:
            params["view"] = pn.Column(
                sizing_mode="stretch_both",
                margin=(0, 0, 0, 0),
                name="Panel Designer View",
                css_classes=["designer-view"],
            )

        super().__init__(**params)

        pn.config.raw_css.append(config.CSS)

        self.designer_pane[:] = [
            self.title_component.view,
            pn.layout.Divider(margin=(20, 10, 10, 10)),
            self.action_pane,
            pn.layout.Divider(margin=(20, 10, 10, 10)),
            pn.Column(
                self.settings_pane,
                css_classes=["designer-settings-scroll"],
                sizing_mode="stretch_both",
                scroll=True,
                max_height=350,
            ),
            pn.layout.Divider(margin=(20, 10, 10, 10)),
            self.stop_server_pane,
            pn.pane.HTML(
                '<link href="https://fonts.googleapis.com/css?family=Roboto:300,400,500&display=swap" rel="stylesheet">'
            ),
            self.css_pane,
            self.js_pane,
        ]

        self.view[:] = [
            pn.Row(self.component_pane, self.designer_pane, sizing_mode="stretch_both"),
        ]

        self.reload_component_instance = self._reload_component_instance
        self.reload_css_file = self._reload_css_file
        self.reload_js_file = self._reload_js_file
        self.show = self._show
        self.stop_server = self._stop_server

        self.reload_component_instance()
        self.reload_css_file()
        self.reload_js_file()

    def _reload_component_instance(self, _=None):
        self.title_component.start_spinning()
        self._update_last_reload()
        try:
            print("reload start", self.name, datetime.datetime.now())
            if self.component is None:
                with param.edit_constant(self):
                    self.component = EmptyComponent

            if self.component_instance is None:
                self.component_instance = self.component(**self.component_parameters)
            else:
                self._reload_component()
                self.component_instance = self.component(**self.component_parameters)

            if isinstance(self.component_instance, pn.layout.Reactive):
                component_view = self.component_instance
            elif hasattr(self.component_instance, "view"):
                component_view = self.component_instance.view
            else:
                raise NotImplementedError

            self.component_pane.component = component_view
            self.component_pane._update()
            self.settings_pane.object = self.component_instance

            print("reload end", self.name, datetime.datetime.now())
        except Exception as ex:
            self.error_pane.object = "# Error " + traceback.format_exc()
            self.component_pane.component = self.error_pane
        self.title_component.stop_spinning()

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

    def __repr__(self):
        return f"PanelDesigner(self.__name__)"

    def __str__(self):
        return f"PanelDesigner(self.__name__)"
