import param
import panel as pn
from awesome_panel.models import Application
from awesome_panel.components import LoadingPageComponent
import pathlib

ROOT_URL = (
    "https://raw.githubusercontent.com/MarcSkovMadsen/awesome-panel/master/assets/images/spinners/"
)

SPINNER_URL = "https://panel.holoviz.org/_static/logo.png"
SPINNER_STATIC_URL = "https://panel.holoviz.org/_static/logo_stacked.png"


class ApplicationTemplate(pn.Template):
    application = param.ClassSelector(class_=Application)
    template_path = param.ClassSelector(class_=pathlib.Path)
    css_path = param.ClassSelector(class_=pathlib.Path)

    select_title_page = param.Action()
    spinning = param.Boolean()

    loading_page_component = param.ClassSelector(class_=LoadingPageComponent)
    _page_instances = param.Dict()

    def __init__(self, **params):
        params["template"] = params["template_path"].read_text()
        if "loading_page_component" not in params:
            params["loading_page_component"]=LoadingPageComponent()
        if "_page_instances" not in params:
            params["_page_instances"] = {}

        super().__init__(**params)

        if self.css_path:
            pn.config.css_files.append(self.css_path.resolve())

        self.menu = pn.Param(self.application.param.menu_item, expand_button=False)
        self.sidebar = pn.Column()
        self.main = pn.Column(
            self.application_page_instance.main, sizing_mode="stretch_both", margin=(25, 50, 25, 50)
        )
        self.theme_css = pn.pane.HTML(height=0, width=0, sizing_mode="fixed", margin=0)
        self.spinner = pn.pane.PNG(SPINNER_STATIC_URL, sizing_mode="fixed", height=40)

        self.add_panel(name="menu_item", panel=self.menu)
        self.add_panel(name="main", panel=self.main)
        self.add_panel(name="theme_css", panel=self.theme_css)
        self.add_panel(name="spinner", panel=self.spinner)

        self.select_title_page = self._select_title_page
        self._set_select_title_page_label()

    @param.depends("application.page", watch=True)
    def _set_main_objects(self):
        # self.loading_page_component.page_component = self.application_page_instance
        self.main[:] = [self.loading_page_component.main]
        self.main[:] = [self.application_page_instance.main]

    @param.depends("application.title", watch=True)
    def _set_select_title_page_label(self):
        self.param.select_title_page.label = self.application.title

    def _select_title_page(self, _=None):
        self.application_page_instance = self.application.param.page.default

    @param.depends("spinning", watch=True)
    def _update_spinner(self):
        if self.spinning:
            self.spinner.object = SPINNER_URL
        else:
            self.spinner.object = SPINNER_STATIC_URL

    @property
    def application_page_instance(self):
        page = self.application.page
        if not page in self._page_instances:
            self._page_instances[page]=page()
        return self._page_instances[page]
