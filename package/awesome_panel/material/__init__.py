import param

from awesome_panel.express.pane.web_component import WebComponent

MWC_ICONS = [
    None,
    "accessibility",
    "code",
    "favorite",
]  # For more icons see https://material.io/resources/icons/?style=baseline


class MWCButton(WebComponent):
    html = param.String("<mwc-button></mwc-button")
    attributes_to_watch = param.Dict({"label": "name", "icon": "icon", "raised": "raised"})

    raised = param.Boolean(default=True)
    icon = param.ObjectSelector(default="favorite", objects=MWC_ICONS, allow_None=True)

    height = param.Integer(default=30)

    # NEW IN THIS EXAMPLE
    events_to_watch = param.Dict({"click": "clicks"})
    clicks = param.Integer()

button = MWCButton()
import panel as pn
import pathlib
pn.config.js_files["awesome-panel"]="static/awesome-panel.js"
pn.Column(button, pn.Param(button.param.clicks)).servable()
