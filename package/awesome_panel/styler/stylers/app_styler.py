import param
import panel as pn

_PARAMETERS_TO_WATCH = [
    "body_color",
    "body_background",
    "body_font_family",
    "bar_color",
    "bar_background",
    "bar_shadow",
    "bar_line",
    "container_color",
    "container_background",
    "container_shadow",
    "container_line",
    "settings_color",
    "settings_background",
    "settings_line_right",
    "settings_line_left",
]


class AppStyler(param.Parameterized):
    _update_css_paused = param.Boolean(True)
    body_color = param.String("#000000")
    body_background = param.String("#ffffff")
    body_font_family = param.String("Times New Roman")

    bar_color = param.String("#ffffff")
    bar_background = param.String("#4caf50")
    bar_shadow = param.Boolean(True)
    bar_line = param.Boolean(False)

    container_color = param.String("#ffffff")
    container_background = param.String("#4caf50")
    container_radius = param.Integer(5, bounds=(0, 25), step=1)
    container_shadow = param.Boolean(True)
    container_line = param.Boolean(False)

    settings_color = param.String("#ffffff")
    settings_background = param.String("#4caf50")
    settings_line_right = param.Boolean(False)
    settings_line_left = param.Boolean(False)

    css = param.String()

    css_pane = param.Parameter()
    view = param.Parameter()

    def __init__(self, **params):
        super().__init__(**params)

        self.css_pane = self._get_css_pane()
        self.view = self._get_view(self.css_pane)

        self._update_css()
        self._update_css_pane()

    def _get_css_pane(self):
        return pn.pane.HTML(
            "ABCD", width=0, height=0, sizing_mode="fixed", margin=0, css_classes=["app-body-css"]
        )

    def _get_view(self, css_pane):
        params = {"sizing_mode": "stretch_width", "show_name": False}
        body_pane = pn.Param(
            self,
            parameters=["body_color", "body_color", "body_background", "body_font_family"],
            **params,
            name="Body",
        )
        bar_pane = pn.Param(
            self,
            parameters=["bar_color", "bar_background", "bar_shadow", "bar_line",],
            **params,
            name="Bar",
        )
        container_pane = pn.Param(
            self,
            parameters=[
                "container_color",
                "container_background",
                "container_radius",
                "container_shadow",
                "container_line",
            ],
            **params,
            name="Container",
        )
        settings_pane = pn.Param(
            self,
            parameters=[
                "settings_color",
                "settings_background",
                "settings_line_right",
                "settings_line_left",
            ],
            **params,
            name="Settings",
        )

        tabs = pn.Tabs(
            body_pane, bar_pane, container_pane, settings_pane, sizing_mode="stretch_width"
        )
        css_edit_pane = pn.Param(
            self,
            parameters=["css"],
            widgets={
                "css": {"type": pn.widgets.Ace, "min_height": 500, "sizing_mode": "stretch_width", "language": "css"}
            },
            sizing_mode="stretch_width",
            show_name=False,
            css_classes=["app-body-css-edit-pane"],
        )
        return pn.Column(
            # css_pane,
            tabs,
            pn.layout.Divider(),
            css_edit_pane,
            sizing_mode="stretch_width",
            name="App",
        )

    @param.depends(*_PARAMETERS_TO_WATCH, watch=True)
    def _update_css(self):
        if self._update_css_paused:
            return

        print("start")
        body_css = f"""\
.bk.app-body {{
    color: {self.body_color};
    background: {self.body_background};
    font-family: {self.body_font_family};
}}"""

        bar_css = f"""\
.bk.app-bar {{
    color: {self.bar_color};
    background: {self.bar_background};"""
        if self.bar_shadow:
            bar_css += "\n    box-shadow: 5px 5px 20px #9E9E9E;"
        if self.bar_line:
            bar_css += "\n        border-bottom: 5px;\n    border-bottom-style: solid;"
        bar_css += "\n}"

        container_css = f"""\
.bk.app-container {{
    color:{self.container_color};
    background:{self.container_background};
    border-radius: {self.container_radius}px;"""
        if self.container_shadow:
            container_css += "\n    box-shadow: 2px 2px 2px lightgrey;"
        if self.container_line:
            container_css += "\n        border: 5px;\n    border-style: solid;"
        container_css += "\n}"

        self.css = body_css + "\n" + bar_css + "\n" + container_css

    @param.depends("css", watch=True)
    def _update_css_pane(self):
        self.css_pane.object = "<style>" + self.css + "</style>"

    def apply_theme(self, theme):
        self._update_css_paused = True
        if theme == "caliber":
            self.bar_background = "#4caf50"
            self.bar_color = "#ffffff"
            self.bar_line = False
            self.bar_shadow = True

            self.body_background = "#f2f2f2"
            self.body_color = "#000000"
            self.body_font_family = "Times New Roman"

            self.container_background = "#ffffff"
            self.container_color = "#000000"
            self.container_line = False
            self.container_radius = 5
            self.container_shadow = True

            self.settings_background = "#fafafa"
            self.settings_color = "#000000"
            self.settings_line_right = True
            self.settings_line_left = False
        elif theme == "light_minimal":
            self.bar_background = "#4caf50"
            self.bar_color = "#ffffff"
            self.bar_line = False
            self.bar_shadow = True

            self.body_background = "#f2f2f2"
            self.body_color = "#000000"
            self.body_font_family = "Times New Roman"

            self.container_background = "#ffffff"
            self.container_color = "#000000"
            self.container_line = False
            self.container_radius = 5
            self.container_shadow = True

            self.settings_background = "#fafafa"
            self.settings_color = "#000000"
            self.settings_line_right = True
            self.settings_line_left = False
        elif theme == "dark_minimal":
            self.bar_background = "#000000"
            self.bar_color = "#ffffff"
            self.bar_line = True
            self.bar_shadow = False

            self.body_background = "#000000"
            self.body_color = "#ffffff"
            self.body_font_family = "Times New Roman"

            self.container_background = "#000000"
            self.container_color = "#ffffff"
            self.container_line = True
            self.container_radius = 5
            self.container_shadow = False

            self.settings_background = "#fafafa"
            self.settings_color = "#000000"
            self.settings_line_right = True
            self.settings_line_left = False
        elif theme == "material-light":
            self.bar_background = "#4caf50"
            self.bar_color = "#ffffff"
            self.bar_line = False
            self.bar_shadow = True

            self.body_background = "#f2f2f2"
            self.body_color = "#000000"
            self.body_font_family = "roboto, sans-serif, Verdana"

            self.container_background = "#ffffff"
            self.container_color = "#000000"
            self.container_line = False
            self.container_radius = 5
            self.container_shadow = True

            self.settings_background = "#fafafa"
            self.settings_color = "#000000"
            self.settings_line_right = True
            self.settings_line_left = False
        elif theme == "material-dark":
            self.bar_background = "#303030"
            self.bar_color = "#ffffff"
            self.bar_shadow = False
            self.bar_line = True

            self.body_background = "#303030"
            self.body_color = "#000000"
            self.body_font_family = "roboto, sans-serif, Verdana"

            self.container_background = "#801797"
            self.container_color = "#ffffff"
            self.container_line = True
            self.container_radius = 5
            self.container_shadow = False

            self.settings_background = "#fafafa"
            self.settings_color = "#000000"
            self.settings_line_right = True
            self.settings_line_left = False
        else:
            raise NotImplementedError(theme)
        self._update_css_paused = False
        self._update_css()


pn.extension("ace")
AppStyler().view.servable()
