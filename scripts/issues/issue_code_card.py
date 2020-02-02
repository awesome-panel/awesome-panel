"""In this module we define cards inspired by

- https://getbootstrap.com/docs/4.3/components/card/ and
- https://disjfa.github.io/bootstrap-tricks/card-collapse-tricks/
"""

from typing import (
    List,
    Union,
)

import panel as pn


class Card(pn.Column):
    """A Card inspired by the Bootstrap Card"""

    def __init__(
        self,
        header: str,
        body: Union[pn.viewable.Viewable, List[pn.viewable.Viewable],],
        **kwargs,
    ):
        if not isinstance(body, list,):
            panels = [body]
        else:
            panels = body

        content = pn.Row(body)
        header_pane = self.get_card_header(header)
        super().__init__(
            header_pane, content, **kwargs,
        )
        return

    def _get_card_content(self, panels: List[pn.viewable.Viewable],) -> pn.viewable.Viewable:
        content = pn.Column(
            *[self.get_card_panel(panel) for panel in panels],
            css_classes=["card-body"],
            sizing_mode="stretch_width",
            margin=(0, 2, 2, 0,),
        )
        return content

    @staticmethod
    def get_card_header(text: str, **kwargs,) -> pn.pane.HTML:
        if "css_classes" not in kwargs:
            kwargs["css_classes"] = []
        if "card-header" not in kwargs["css_classes"]:
            kwargs["css_classes"].append("card-header")
        if "sizing_mode" not in kwargs and "width" not in kwargs:
            kwargs["sizing_mode"] = "stretch_width"
        if "margin" not in kwargs:
            kwargs["margin"] = 0
        object_ = f'<h5 class="card-header"">{text}</h5>'

        return pn.pane.HTML(object_, **kwargs,)

    @staticmethod
    def get_card_panel(obj, **kwargs,) -> pn.viewable.Viewable:
        return pn.panel(obj, **kwargs,)

import param
class Dummy(param.Parameterized):
    value = param.Parameter("abcd")

dummy = Dummy()
@param.depends(dummy.param.value)
def get_card(value):
    return Card("Code", pn.pane.HTML(f"<strong>{value}</strong>"))

pn.Column(get_card).servable()