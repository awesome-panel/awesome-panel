import param
import panel as pn
import pathlib


class ApplicationView(pn.Template):
    # template_path = param.ClassSelector(class_=pathlib.Path, allow_None=False, constant=True)
    # css_path = param.ClassSelector(class_=pathlib.Path, allow_None=False, constant=True)

    main = param.ClassSelector(class_=pn.layout.Reactive, allow_None=False, constant=True)
    sidebar = param.ClassSelector(class_=pn.layout.Reactive, allow_None=False, constant=True)
    topbar = param.ClassSelector(class_=pn.layout.Reactive, allow_None=False, constant=True)
    spinner = param.ClassSelector(class_=pn.layout.Reactive, allow_None=False, constant=True)
    navigation = param.ClassSelector(class_=pn.layout.Reactive, allow_None=False, constant=True)

    application_css = param.ClassSelector(class_=pn.pane.HTML, allow_None=False, constant=True)
    application_js = param.ClassSelector(class_=pn.pane.HTML, allow_None=False, constant=True)

    theme_css = param.ClassSelector(class_=pn.pane.HTML, allow_None=False, constant=True)
    theme_js = param.ClassSelector(class_=pn.pane.HTML, allow_None=False, constant=True)

    page_css = param.ClassSelector(class_=pn.pane.HTML, allow_None=False, constant=True)
    page_js = param.ClassSelector(class_=pn.pane.HTML, allow_None=False, constant=True)

    def __init__(self, **params):
        # if "template" not in params:
        #     params["template"] = params["template_path"].read_text()
        if "main" not in params:
            params["main"] = self._get_main()
        if "sidebar" not in params:
            params["sidebar"] = self._get_sidebar()
        if "topbar" not in params:
            params["topbar"] = self._get_topbar()
        if "spinner" not in params:
            params["spinner"] = self._get_spinner()
        if "navigation" not in params:
            params["navigation"] = self._get_navigation()
        if "application_css" not in params:
            params["application_css"] = self._get_invisible_html_pane("aplication_css")
        if "application_js" not in params:
            params["application_js"] = self._get_invisible_html_pane("aplication_js")
        if "theme_css" not in params:
            params["theme_css"] = self._get_invisible_html_pane("theme_css")
        if "theme_js" not in params:
            params["theme_js"] = self._get_invisible_html_pane("theme_js")
        if "page_css" not in params:
            params["page_css"] = self._get_invisible_html_pane("page_css")
        if "page_js" not in params:
            params["page_js"] = self._get_invisible_html_pane("page_js")

        super().__init__(**params)

        self.add_panel(name="main", panel=self.main)
        self.add_panel(name="sidebar", panel=self.sidebar)
        self.add_panel(name="topbar", panel=self.topbar)
        self.add_panel(name="spinner", panel=self.spinner)
        self.add_panel(name="navigation", panel=self.navigation)
        self.add_panel(name="application_css", panel=self.application_css)
        self.add_panel(name="application_js", panel=self.application_js)
        self.add_panel(name="theme_css", panel=self.theme_css)
        self.add_panel(name="theme_js", panel=self.theme_js)
        self.add_panel(name="page_css", panel=self.page_css)
        self.add_panel(name="page_js", panel=self.page_js)

    @staticmethod
    def _get_main():
        return pn.Column(
            name="ApplicationComponent.main",
            css_classes=["main"],
            sizing_mode="stretch_both",
            margin=(25, 50, 50, 50),
        )

    @staticmethod
    def _get_sidebar():
        return pn.Column(name="ApplicationComponent.sidebar")

    @staticmethod
    def _get_topbar():
        return pn.Row(name="ApplicationComponent.topbar", sizing_mode="stretch_width")

    @staticmethod
    def _get_navigation():
        return pn.Row(name="ApplicationComponent.navigation", sizing_mode="stretch_width")

    @staticmethod
    def _get_spinner():
        return pn.Column(name="ApplicationComponent.spinner", sizing_mode="stretch_both")

    @staticmethod
    def _get_invisible_html_pane(name):
        name = f"ApplicationComponent.{name.lower()}"
        return pn.pane.HTML(name=name, height=0, width=0, sizing_mode="fixed", margin=0)
