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

button = MWCButton(name="Click me")
import panel as pn
import pathlib
JS = "https://cdn.jsdelivr.net/gh/marcskovmadsen/awesome-panel@96c60e21de6d6a0e7ecc275980c55715c4bda108/assets/js/awesome-panel.min.js"
MATERIAL = "https://cdn.jsdelivr.net/gh/marcskovmadsen/awesome-panel@be59521090b7c9d9ba5eb16e936034e412e2c86b/assets/js/mwc.bundled.js"
pn.config.js_files["material"]=MATERIAL
pn.config.js_files["awesome-panel"]=JS
pn.Column(button, pn.Param(button.param.clicks)).servable()
