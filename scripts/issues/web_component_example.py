import panel as pn
import param

from awesome_panel_extensions.pane import WebComponent

MWC_ICONS = [
    None,
    "accessibility",
    "code",
    "favorite",
]  # For more icons see https://material.io/resources/icons/?style=baseline


class MWCButton(WebComponent):
    html = param.String("<mwc-button></mwc-button")
    attributes_to_watch = param.Dict({"label": "name", "icon": "icon", "raised": "raised"})
    events_to_watch = param.Dict({"click": "clicks"})

    raised = param.Boolean(default=True)
    icon = param.ObjectSelector(default="favorite", objects=MWC_ICONS, allow_None=True)
    clicks = param.Integer()

    height = param.Integer(default=30)


mwc_button = MWCButton(name="Click Me!")

MWC_EXTENSIONS = """
<script type='module' src='https://www.unpkg.com/@material/mwc-button?module'></script>
<link href='https://fonts.googleapis.com/css?family=Roboto:300,400,500' rel='stylesheet'>
<link href='https://fonts.googleapis.com/css?family=Material+Icons&display=block' rel='stylesheet'>
<style>
:root {
    --mdc-theme-primary: green;
    --mdc-theme-secondary: purple*;
}
</style>
"""

extensions_pane = pn.pane.Markdown(MWC_EXTENSIONS, height=0, width=0, sizing_mode="fixed", margin=0)
settings_pane = pn.Param(mwc_button, parameters=["name", "icon", "raised", "height", "clicks"])
app = pn.Column(extensions_pane, mwc_button, settings_pane)

app.servable()  # Launch with the `panel serve <name-of-file.py>` command
