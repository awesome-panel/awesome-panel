"""The SiteSettings contains a collecation of user definable settings"""
import panel as pn
import param
from awesome_panel_extensions.models.icon import Icon
from awesome_panel_extensions.widgets.button import AwesomeButton

from application.shared.logger import get_logger

logger = get_logger(__name__)

PARAMETERS = ["theme", "template"]

# pylint: disable=line-too-long
DEFAULT_ICON = Icon(
    name="Sun",
    value="""<svg width="1em" height="1em" viewBox="0 0 16 16" class="bi bi-sun" fill="currentColor" xmlns="http://www.w3.org/2000/svg"><path d="M3.5 8a4.5 4.5 0 1 1 9 0 4.5 4.5 0 0 1-9 0z"/><path fill-rule="evenodd" d="M8.202.28a.25.25 0 0 0-.404 0l-.91 1.255a.25.25 0 0 1-.334.067L5.232.79a.25.25 0 0 0-.374.155l-.36 1.508a.25.25 0 0 1-.282.19l-1.532-.245a.25.25 0 0 0-.286.286l.244 1.532a.25.25 0 0 1-.189.282l-1.509.36a.25.25 0 0 0-.154.374l.812 1.322a.25.25 0 0 1-.067.333l-1.256.91a.25.25 0 0 0 0 .405l1.256.91a.25.25 0 0 1 .067.334L.79 10.768a.25.25 0 0 0 .154.374l1.51.36a.25.25 0 0 1 .188.282l-.244 1.532a.25.25 0 0 0 .286.286l1.532-.244a.25.25 0 0 1 .282.189l.36 1.508a.25.25 0 0 0 .374.155l1.322-.812a.25.25 0 0 1 .333.067l.91 1.256a.25.25 0 0 0 .405 0l.91-1.256a.25.25 0 0 1 .334-.067l1.322.812a.25.25 0 0 0 .374-.155l.36-1.508a.25.25 0 0 1 .282-.19l1.532.245a.25.25 0 0 0 .286-.286l-.244-1.532a.25.25 0 0 1 .189-.282l1.508-.36a.25.25 0 0 0 .155-.374l-.812-1.322a.25.25 0 0 1 .067-.333l1.256-.91a.25.25 0 0 0 0-.405l-1.256-.91a.25.25 0 0 1-.067-.334l.812-1.322a.25.25 0 0 0-.155-.374l-1.508-.36a.25.25 0 0 1-.19-.282l.245-1.532a.25.25 0 0 0-.286-.286l-1.532.244a.25.25 0 0 1-.282-.189l-.36-1.508a.25.25 0 0 0-.374-.155l-1.322.812a.25.25 0 0 1-.333-.067L8.203.28zM8 2.5a5.5 5.5 0 1 0 0 11 5.5 5.5 0 0 0 0-11z"/></svg>""",
    fill_color="#FF9800",
)

DARK_ICON = Icon(
    name="Github",
    value="""<svg width="1em" height="1em" viewBox="0 0 16 16" class="bi bi-moon" fill="currentColor" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M14.53 10.53a7 7 0 0 1-9.058-9.058A7.003 7.003 0 0 0 8 15a7.002 7.002 0 0 0 6.53-4.47z"/></svg>""",
    fill_color="black",
)
# pylint: enable=line-too-long
class TemplateSettings(param.Parameterized):
    """Collection of user definable settings"""

    toggle_theme = param.Action(label="")
    theme = param.ObjectSelector("default", objects=["default", "dark"])
    template = param.ObjectSelector(
        "material", objects=["bootstrap", "golden", "material", "react", "vanilla"]
    )

    settings_panel = param.Parameter()
    js_panel = param.Parameter()
    view = param.Parameter()

    def __init__(self, parameters=None, **params):
        logger.info("Initializing Settings %s", pn.state.session_args)
        self._update_param_from_session_args("theme", params)
        self._update_param_from_session_args("template", params)
        super().__init__(**params)

        if not parameters:
            parameters = PARAMETERS
        parameters = [*parameters]

        if "theme" in parameters:
            parameters.append("toggle_theme")
        parameters = [p for p in parameters if p != "theme"]

        self.toggle_theme = self._toggle_theme

        self._create_panels_and_view(parameters)

    def _create_panels_and_view(self, parameters):
        if self.theme == "dark":
            icon = DARK_ICON
        else:
            icon = DEFAULT_ICON

        self.settings_panel = pn.Param(
            self,
            parameters=parameters,
            widgets={
                "template": {"width": 100, "sizing_mode": "fixed"},
                "toggle_theme": {
                    "type": AwesomeButton,
                    "width": 50,
                    "sizing_mode": "fixed",
                    "icon": icon,
                },
            },
            default_layout=pn.Row,
            show_labels=False,
            show_name=False,
            sizing_mode="fixed",
            width=200,
            css_classes=["template-settings"],
        )

        if self.js_panel:
            self.view = self.settings_panel
        else:
            self.js_panel = pn.pane.HTML(height=0, width=0, margin=0, sizing_mode="fixed")
            self.view = pn.Row(self.settings_panel, self.js_panel, sizing_mode="fixed", width=200)

    def _update_param_from_session_args(self, parameter, params):
        if parameter in pn.state.session_args:
            value = pn.state.session_args[parameter][0].decode("utf-8")
            value = value.strip("'").strip('"').replace("%22", "")
            if value in self.param[parameter].objects:
                params[parameter] = value

    def _toggle_theme(self, *_):
        if self.theme == "default":
            self.theme = "dark"
        else:
            self.theme = "default"

    @param.depends("theme", "template", watch=True)
    def _change_query_params(self, *_):
        pn.state.location.update_query(template=self.template, theme=self.theme)
        logger.info("reload to %s", pn.state.location.query_params)
        self.js_panel.object = "<script>location.reload()</script>"


if __name__.startswith("bokeh"):
    TemplateSettings().view.servable()
