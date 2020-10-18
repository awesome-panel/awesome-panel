"""In this module we define the ApplicationTemplate.

This is an abstract, base class. Use an implementation like MaterialTemplate"""
import pathlib

import panel as pn
import param
from awesome_panel.application.components import (
    LoadingPageComponent,
    PageComponent,
    ProgressSpinnerComponent,
)
from awesome_panel.application.models import Application
from awesome_panel.application.services import Services


class ApplicationTemplate(pn.Template):
    """The ApplicationTemplate implements the common functionality to be used by all Templates

    This is an abstract, base class. Use an implementation like MaterialTemplate"""

    application = param.ClassSelector(class_=Application)
    template_path = param.ClassSelector(class_=pathlib.Path)
    css_path = param.ClassSelector(class_=pathlib.Path)

    select_title_page = param.Action()
    main_max_width = param.Integer(default=1140)

    loading_page_component = param.ClassSelector(class_=LoadingPageComponent, constant=True)
    _page_instances = param.Dict()

    services = param.ClassSelector(class_=Services)

    def __init__(self, **params):
        pn.config.sizing_mode = "stretch_width"

        params["template"] = params["template_path"].read_text()
        if "services" not in params:
            params["services"] = Services()
        if "loading_page_component" not in params:
            services = params["services"]
            params["loading_page_component"] = LoadingPageComponent(
                progress_service=services.progress_service, theme_service=services.theme_service
            )
        if "_page_instances" not in params:
            params["_page_instances"] = {}
        super().__init__(**params)

        if self.css_path:
            pn.config.css_files.append(self.css_path.resolve())

        self.spinner = ProgressSpinnerComponent(
            progress_service=self.services.progress_service,
            theme_service=self.services.theme_service,
        ).view
        self.spinner.sizing_mode = "fixed"
        self.spinner.height = 40
        self.sidebar = pn.Column()
        self._main_spacer = pn.Spacer(height=0, margin=0)
        self.main = pn.Column(
            name="main",
            css_classes=["main"],
            sizing_mode="stretch_both",
            margin=(25, 50, 50, 50),
        )
        self._update_main_container()
        self.template_css = pn.pane.HTML(height=0, width=0, sizing_mode="fixed", margin=0)

        self.add_panel(name="sidebar", panel=self.sidebar)
        self.add_panel(name="main", panel=self.main)
        self.add_panel(name="template_css", panel=self.template_css)
        self.add_panel(name="spinner", panel=self.spinner)

        self.select_title_page = self._select_title_page
        self._set_select_title_page_label()

    @param.depends("services.page_service.page", watch=True)
    def _update_main_container(self):
        with self.services.progress_service.mark_active(
            f"Loading {self.services.page_service.page.name}"
        ):
            if self.services.page_service.page.show_loading_page:
                self.main[:] = [self.loading_page_component.main]

            main_instance = self._application_page_instance.main
            main_instance.align = "center"
            main_instance.sizing_mode = "stretch_width"

            self.main[:] = [
                self._main_spacer,  # Trick to force main to stretch to full width of appContent
                main_instance,
            ]

    @param.depends("application.title", watch=True)
    def _set_select_title_page_label(self):
        self.param.select_title_page.label = self.application.title

    def _select_title_page(self, _=None):
        self.services.page_service.page = self.services.page_service.default_page

    @property
    def _application_page_instance(self):
        # pylint: disable=unsubscriptable-object,unsupported-membership-test
        # pylint: disable=unsupported-assignment-operation
        page = self.services.page_service.page
        if not page in self._page_instances:
            instance = PageComponent.create(page.component)
            self._page_instances[page] = instance

            if instance.main and not isinstance(instance.main, pn.reactive.Reactive):
                instance.main = pn.panel(instance.main)
            if instance.sidebar and not isinstance(instance.sidebar, pn.reactive.Reactive):
                instance.sidebar = pn.panel(instance.sidebar)

            if instance.main and self.services.page_service.page.restrict_max_width:
                instance.main.max_width = 1140
            else:
                instance.main.max_width = None

        return self._page_instances[page]
