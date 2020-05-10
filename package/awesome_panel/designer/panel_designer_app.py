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
from awesome_panel.designer.services import ReloadService

ACTION_PANE_INDEX = 3


class PanelDesignerApp(param.Parameterized):
    reload_service = param.ObjectSelector(label="Component")

    action_pane = param.ClassSelector(class_=pn.Param, constant=True)
    settings_pane = param.ClassSelector(class_=pn.Param, constant=True)
    settings_scroll_pane = param.ClassSelector(class_=pn.Column, constant=True)
    font_pane = param.ClassSelector(class_=pn.pane.HTML, constant=True)

    css_pane = param.ClassSelector(class_=pn.pane.HTML, constant=True)
    js_pane = param.ClassSelector(class_=pn.pane.HTML, constant=True)
    error_pane = param.ClassSelector(class_=pn.pane.Markdown, constant=True)

    title_component = param.ClassSelector(
        class_=TitleComponent, constant=True, label="Title Component"
    )

    designer_pane = param.ClassSelector(class_=pn.WidgetBox, constant=True)
    component_pane = param.ClassSelector(class_=CenteredComponent, constant=True)
    stop_server_pane = param.ClassSelector(class_=pn.Param, constant=True)

    view = param.ClassSelector(class_=pn.Row, constant=True)

    show = param.Action(label="SHOW")
    stop_server = param.Action(label="STOP SERVER AND EXIT")

    server = param.Parameter(constant=True)

    def __init__(self, reload_services):
        pn.config.raw_css.append(config.CSS)

        self.param.reload_service.objects = reload_services
        self.param.reload_service.default = reload_services[0]

        super().__init__(reload_services=reload_services)

        with param.edit_constant(self):
            self.name = "Panel Designer App"
            self.title_component = TitleComponent()
            self.css_pane = self._create_css_pane()
            self.js_pane = self._create_js_pane()
            self.component_pane = self._create_component_pane()
            self.action_pane = self._create_action_pane()
            self.settings_pane = self._create_settings_pane()
            self.settings_scroll_pane = self._create_settings_scroll_pane(self.settings_pane)
            self.font_pane = self._create_font_pane()
            self.error_pane = self._create_error_pane()
            self.stop_server_pane = self._create_stop_server_pane()
            self.designer_pane = self._create_designer_pane(
                title_component=self.title_component,
                action_pane=self.action_pane,
                settings_scroll_pane=self.settings_scroll_pane,
                stop_server_pane=self.stop_server_pane,
                font_pane=self.font_pane,
                css_pane=self.css_pane,
                js_pane=self.js_pane,
            )
            self.view = self._create_view(self.component_pane, self.designer_pane)
            self.show = self._show
            self.stop_server = self._stop_server

        self._create_watchers(reload_services)
        self._handle_reload_service_change()

    def _create_watchers(self, reload_services):
        for reload_service in reload_services:
            reload_service.param.watch(self._update_component, ["component_instance"], onlychanged=True)
            reload_service.param.watch(self._update_css_pane, ["css_text"], onlychanged=True)
            reload_service.param.watch(self._update_js_pane, ["js_text"], onlychanged=True)

    @param.depends("reload_service", watch=True)
    def _handle_reload_service_change(self):
        self.reload_service.reload_component()
        self.reload_service.reload_css_file()
        self.reload_service.reload_js_file()

        self._update_component()
        self._update_css_pane()
        self._update_js_pane()

    def _update_component(self, *events):
        action_pane_index = self.designer_pane.objects.index(self.action_pane)
        with param.edit_constant(self):
            self.action_pane = self._create_action_pane()
        self.designer_pane[action_pane_index] = self.action_pane

        if self.reload_service.error_message:
            self._set_error_message()
            return

        if self.reload_service.component_instance:
            self.settings_pane.object = self.reload_service.component_instance

            if isinstance(self.reload_service.component_instance, pn.layout.Reactive):
                component_view = self.reload_service.component_instance
            elif hasattr(self.reload_service.component_instance, "view"):
                component_view = self.reload_service.component_instance.view
            else:
                raise NotImplementedError

            self.component_pane.component = component_view
            self.component_pane._update()

        print("_update_component", self.reload_service)

    def _update_css_pane(self, *events):
        self.css_pane.object = f"<style>{self.reload_service.css_text}</style>"
        if self.reload_service.error_message:
            self._set_error_message()
        print("_update_css_pane", self.reload_service)

    def _update_js_pane(self, *events):
        self.js_pane.object = f"<script>{self.reload_service.js_text}</script>"
        if self.reload_service.error_message:
            self._set_error_message()
        print("_update_js_pane", self.reload_service)

    def _set_error_message(self):
        component_view = pn.pane.Markdown(self.reload_service.error_message)
        self.component_pane.component = component_view
        self.component_pane._update()

    @staticmethod
    def _create_css_pane():
        return pn.pane.HTML(
            name="CSS Pane",
            sizing_mode="fixed",
            width=0,
            height=0,
            margin=0,
            css_classes=["designer-css-pane"],
        )

    @staticmethod
    def _create_js_pane():
        return pn.pane.HTML(
            name="JS Pane",
            sizing_mode="fixed",
            width=0,
            height=0,
            margin=0,
            css_classes=["designer-js-pane"],
        )

    @staticmethod
    def _create_component_pane():
        return CenteredComponent(
            pn.pane.Markdown("hello"),
            name="Component Pane",
            sizing_mode="stretch_both",
            css_classes=["designer-component-pane"],
        )

    def _create_designer_pane(
        self,
        title_component,
        action_pane,
        settings_scroll_pane,
        stop_server_pane,
        font_pane,
        css_pane,
        js_pane,
    ):

        return pn.WidgetBox(
            title_component.view,
            pn.layout.Divider(margin=(20, 10, 10, 10)),
            pn.Param(
                self,
                parameters=["reload_service"],
                show_name=False,
                expand_button=False,
                sizing_mode="stretch_width",
            ),
            action_pane,
            pn.layout.Divider(margin=(20, 10, 10, 10)),
            settings_scroll_pane,
            pn.layout.Divider(margin=(20, 10, 10, 10)),
            stop_server_pane,
            font_pane,
            css_pane,
            js_pane,
            name="Designer Pane",
            sizing_mode="stretch_height",
            width=410,
            background="#F5F5F5",
            margin=(0, 0, 0, 0),
            css_classes=["designer-design-pane"],
        )

    def _create_action_pane(self):

        widgets = {
            "reload_component": {
                "button_type": "success",
                "disabled": not self.reload_service.component,
            },
            "reload_css_file": {"disabled": not self.reload_service.css_path},
            "reload_js_file": {"disabled": not self.reload_service.js_path},
        }

        return pn.Param(
            self.reload_service,
            name="Action Pane",
            sizing_mode="stretch_width",
            parameters=config.ACTION_PARAMETERS,
            widgets=widgets,
            show_name=False,
            css_classes=["designer-action-pane"],
        )

    def _create_settings_pane(self):
        return pn.Param(
            name="Settings Pane",
            sizing_mode="stretch_both",
            css_classes=["designer-settings-pane"],
            margin=(10, 25, 10, 5),
            show_name=False,
        )

    @staticmethod
    def _create_settings_scroll_pane(settings_pane):
        return pn.Column(
            settings_pane,
            name="Settings Scroll Pane",
            css_classes=["designer-settings-scroll"],
            sizing_mode="stretch_width",
            scroll=True,
            height=300,
        )

    @staticmethod
    def _create_error_pane():
        return pn.pane.Markdown(
            name="Error Pane", sizing_mode="stretch_both", css_classes=["designer-error-pane"]
        )

    def _create_stop_server_pane(self):
        return pn.Param(
            self,
            name="Stop Server Pane",
            parameters=["stop_server"],
            widgets={"stop_server": {"button_type": "danger"}},
            sizing_mode="stretch_width",
            show_name=False,
        )

    @staticmethod
    def _create_view(component_pane, designer_pane):
        return pn.Row(
            component_pane,
            designer_pane,
            name="Panel Designer View",
            sizing_mode="stretch_both",
            margin=(0, 0, 0, 0),
            css_classes=["designer-view"],
        )

    @staticmethod
    def _create_font_pane():
        return pn.pane.HTML(
            '<link href="https://fonts.googleapis.com/css?family=Roboto:300,400,500&display=swap" rel="stylesheet">'
        )

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
        return f"PanelDesigner({self.name})"

    def __str__(self):
        return f"PanelDesigner({self.name})"
