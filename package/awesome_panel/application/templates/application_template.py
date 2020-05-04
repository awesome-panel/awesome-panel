import param
import panel as pn
from awesome_panel.application.models import Application, Theme
from awesome_panel.application.components import LoadingPageComponent, PageComponent, ProgressSpinnerComponent
import pathlib
from awesome_panel.application.services import PAGE_SERVICE, progress_service, ProgressService

ROOT_URL = (
    "https://raw.githubusercontent.com/MarcSkovMadsen/awesome-panel/master/assets/images/spinners/"
)

SPINNER_URL = "https://panel.holoviz.org/_static/logo.png"
SPINNER_STATIC_URL = "https://panel.holoviz.org/_static/logo_stacked.png"


STATIC = "<img src='https://github.com/MarcSkovMadsen/awesome-panel/raw/master/assets/images/spinners/spinner_panel_static_light_400_340.gif' style='height:100%' title=''></img>"
BREATH = "<img src='https://github.com/MarcSkovMadsen/awesome-panel/raw/master/assets/images/spinners/spinner_panel_breath_light_400_340.gif' style='height:100%' title=''></img>"

class Spinner(pn.pane.HTML):
    spinning = param.Boolean(default=False)
    static_url = param.String(STATIC)
    spinning_url = param.String(BREATH)

    def __init__(self, **params):
        super().__init__(**params)

        self._update()

    def _update(self, _=None):
        if self.spinning:
            self.object = BREATH
        else:
            self.object = STATIC

class ApplicationTemplate(pn.Template):
    application = param.ClassSelector(class_=Application)
    template_path = param.ClassSelector(class_=pathlib.Path)
    css_path = param.ClassSelector(class_=pathlib.Path)

    select_title_page = param.Action()
    main_max_width = param.Integer(default=1140)

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

        self.spinner = ProgressSpinnerComponent().view
        self.spinner.sizing_mode="fixed"
        self.spinner.height=40
        self.menu = pn.Param(self.application.param.menu_item, expand_button=False)
        self.sidebar = pn.Column()
        self._main_spacer = pn.Spacer(height=0, margin=0)
        self.main = pn.Column(
            name="main", css_classes=["main"],
            sizing_mode="stretch_both",
            margin=(25, 50, 50, 50),
        )
        self._update_main_container()
        self.template_css = pn.pane.HTML(height=0, width=0, sizing_mode="fixed", margin=0)


        self.add_panel(name="menu_item", panel=self.menu)
        self.add_panel(name="main", panel=self.main)
        self.add_panel(name="template_css", panel=self.template_css)
        self.add_panel(name="spinner", panel=self.spinner)

        self.select_title_page = self._select_title_page
        self._set_select_title_page_label()

        if PAGE_SERVICE.default_page:
            self.application.param.page.default=PAGE_SERVICE.default_page
            self.application.page = PAGE_SERVICE.default_page

    @param.depends("application.page", watch=True)
    def _update_main_container(self):
        with progress_service.mark_active(f"Loading {self.application.page.name}"):
            if self.application.page.show_loading_page:
                self.main[:] = [self.loading_page_component.main]

            main_instance = self.application_page_instance.main
            main_instance.align="center"
            main_instance.sizing_mode="stretch_width"

            self.main[:] = [
                self._main_spacer, # Trick to force main to stretch to full width of appContent
                main_instance]

    @param.depends("application.title", watch=True)
    def _set_select_title_page_label(self):
        self.param.select_title_page.label = self.application.title

    def _select_title_page(self, _=None):
        self.application.page = self.application.param.page.default

    @property
    def application_page_instance(self):
        page = self.application.page
        if not page in self._page_instances:
            instance = PageComponent.create(page.component)
            self._page_instances[page]=instance

            # Todo: Setup test and refactor
            if instance.main and not isinstance(instance.main, pn.layout.Reactive):
                instance.main = pn.panel(instance.main)
            if instance.sidebar and not isinstance(instance.sidebar, pn.layout.Reactive):
                instance.sidebar = pn.panel(instance.sidebar)

            if instance.main and self.application.page.restrict_max_width:
                instance.main.max_width=1140
            else:
                instance.main.max_width=None

        return self._page_instances[page]


