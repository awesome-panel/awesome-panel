import panel as pn
import param
from .component import Component
from .page_component import PageComponent

ROOT_URL = (
    "https://raw.githubusercontent.com/MarcSkovMadsen/awesome-panel/master/assets/images/spinners/"
)
SPINNER_URL = ROOT_URL + "spinner_panel_rotate_400_400.gif"
SPINNER_STATIC_URL = ROOT_URL + "spinner_panel_static_light_400_340.gif"


class ChangePageComponent(Component):
    page_component = param.ClassSelector(class_=PageComponent)

    def __init__(self, **params):
        super().__init__(**params)

        self._spinner = pn.pane.GIF(SPINNER_URL, embed=False)
        self._text = pn.pane.HTML()
        self._update()

    @param.depends("page_component", watch="True")
    def _update(self):
        if self.page_component:
            name = "Loading" # self.page_component.name
        else:
            name = "Loading"

        text = f'<marquee id="pageChanging" direction="right" scrollamount="20" behavior="alternate">{name}</marquee>'

        self._text.object = text

    def view(self, **params):
        return pn.Column(
            pn.Row(pn.layout.HSpacer(), self._spinner, pn.layout.HSpacer(), margin=(100,0,0,0)),
            # pn.Row(pn.layout.HSpacer(), self._text, pn.layout.HSpacer()),
            )
