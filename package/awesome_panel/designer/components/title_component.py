import param
import panel as pn
from awesome_panel.application import assets


class TitleComponent(param.Parameterized):
    title = param.String("Panel Designer")
    title_url = param.String("https://panel.holoviz.org")
    subtitle = param.String("awesome-panel.org")
    subtitle_url = param.String("https://awesome-panel.org")
    logo_url = param.String(assets.SPINNER_PANEL_STATIC_LIGHT_400_340)
    logo_spinning_url = param.String(assets.SPINNER_PANEL_BREATH_LIGHT_400_340)
    spinning = param.Boolean(False)
    start_spinning = param.Action(label="Start Spinning")
    stop_spinning = param.Action(label="Stop Spinning")

    spinner_pane = param.Parameter()
    title_pane = param.ClassSelector(class_=pn.pane.HTML)
    view = param.ClassSelector(class_=pn.Row)

    def __init__(
        self, **params,
    ):
        params["start_spinning"] = self._start_spinning
        params["stop_spinning"] = self._stop_spinning

        super().__init__(**params)

        self.title_pane = pn.pane.HTML(margin=(5, 5, 10, 15), sizing_mode="stretch_width")
        self._update_title_pane()

        self.spinner_pane = pn.pane.HTML(
            sizing_mode="fixed", width=70, height=70, align="center", margin=(5, 50, 10, 5)
        )
        self._updatespinner_pane()
        self.view = pn.Row(
            self.title_pane,
            self.spinner_pane,
            name="TitleComponent.view",
            sizing_mode="stretch_width",
            css_classes=["designer-title-component"],
        )

    @param.depends("title", "title_url", "subtitle", "subtitle_url", "logo_url", "logo_spinning_url", watch=True)
    def _update_title_pane(self):
        html = f"""\
<h1><a href="{self.title_url}" target="_blank">{self.title}</a></h1>
<p>By <strong><a href="{self.subtitle_url}" target="_blank">{self.subtitle}</a></strong></p>
"""
        self.title_pane.object = html

    @param.depends("spinning", watch=True)
    def _updatespinner_pane(self):
        if self.spinning:
            url = self.logo_spinning_url
        else:
            url = self.logo_url

        html = f"""
<a href="https://panel.holoviz.org" target="_blank">
<img src="{url}" style="max-height:100%;max-width:100%"></img>
</a>
"""

        # html = f"<img src='{url}' style='width:100%'></img>"
        self.spinner_pane.object = html

    def _start_spinning(self, _=None):
        self.spinning = True

    def _stop_spinning(self, _=None):
        self.spinning = False
