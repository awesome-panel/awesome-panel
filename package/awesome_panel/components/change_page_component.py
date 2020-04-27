import panel as pn
import param
from .component import Component
from .page_component import PageComponent

ROOT_URL = (
    "https://raw.githubusercontent.com/MarcSkovMadsen/awesome-panel/master/assets/images/spinners/"
)
SPINNER_URL = ROOT_URL + "spinner_panel_green_light.gif"
SPINNER_STATIC_URL = ROOT_URL + "spinner_panel_green_light_static.gif"

class ChangePageComponent(Component):
    page_component = param.ClassSelector(class_=PageComponent)

    def __init__(self, **params):
        super().__init__(**params)

        self._spinner = pn.pane.GIF(SPINNER_URL)
        self._text = pn.pane.HTML()
        self._update()

    @param.depends("page_component", watch="True")
    def _update(self):
        if self.page_component:
            name = self.page_component.name
        else:
            name = "Loading ..."

        text = f'<marquee id="pageChanging" direction="right" scrollamount="20" behavior="alternate">{name}</marquee>'

        self._text.object = text

    def view(self, **params):
        content = pn.GridSpec(height=200, sizing_mode="stretch_width")
        content[0, 0]=pn.layout.Spacer()
        content[0, 1:3]=self._text
        content[0, 3]=pn.layout.Spacer()

        return pn.Column(
            pn.layout.VSpacer(),
            content,
            pn.layout.VSpacer(),
            sizing_mode="stretch_both",
        )