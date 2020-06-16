import param
import panel as pn

PRETTY_CONTAINER_CSS_CLASS = "app-container"
PRETTY_CONTAINER_MARGIN = 25
class PrettyContainer(pn.Column):
    def __init__(self, args, **params):
        params["css_classes"]=params.get("css_classes", [])
        params["margin"]=params.get("margin", PRETTY_CONTAINER_MARGIN)
        if not PRETTY_CONTAINER_CSS_CLASS in params["css_classes"]:
            params["css_classes"].append(PRETTY_CONTAINER_CSS_CLASS)

        super().__init__(*args, **params)

class InfoCard(PrettyContainer):
    value = param.Number(default=0)
    text = param.String(default="")

    def __init__(self, **params):
        self._rename = {
            **self._rename,
            "value": None,
            "text": None,
        }
        self._markdown_pane = pn.pane.Markdown(
            sizing_mode="stretch_width",
            margin=15,
        )
        params["sizing_mode"]=params.get("sizing_mode", "stretch_both")
        super().__init__(self._markdown_pane, **params)


        self._update()

    @param.depends("value", "text", watch=True)
    def _update(self):
        self._markdown_pane.object = self._get_text(self.value, self.text)

    @staticmethod
    def _get_text(value, text):
        return f"""\
#### {value}

{text}
"""






