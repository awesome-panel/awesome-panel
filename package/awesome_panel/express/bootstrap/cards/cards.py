"""In this module we define cards inspired by

- https://getbootstrap.com/docs/4.3/components/card/ and
- https://disjfa.github.io/bootstrap-tricks/card-collapse-tricks/
"""

from typing import List, Union

import panel as pn


class Card(pn.Column):
    """A Card inspired by the Bootstrap Card"""

    def __init__(
        self,
        header: str,
        body: Union[pn.viewable.Viewable, List[pn.viewable.Viewable],],
        collapsable: bool = False,
        **kwargs,
    ):
        if "css_classes" not in kwargs:
            kwargs["css_classes"] = []
        if "card" not in kwargs["css_classes"]:
            kwargs["css_classes"].append("card")
        if "sizing_mode" not in kwargs and "width" not in kwargs:
            kwargs["sizing_mode"] = "stretch_width"
        if not isinstance(body, list,):
            panels = [body]
        else:
            panels = body

        # Due to https://github.com/holoviz/panel/issues/903 we have to insert the content into a
        # column with relevant margin
        #
        content = self._get_card_content(panels)

        if not collapsable:
            header_pane = self.get_card_header(header)
            super().__init__(
                header_pane, content, **kwargs,
            )
            return

        collapse_button = pn.widgets.Button(
            name="-", width=30, sizing_mode="stretch_height", css_classes=["flat"],
        )

        def click_callback(event,):
            if event.new % 2 == 1:
                self.remove(content)
                collapse_button.name = "+"
            elif event.new > 0:
                self.append(content)
                collapse_button.name = "-"

        collapse_button.on_click(click_callback)
        header_row = pn.Row(
            f'<h5 class="card-header"">{header}</h5>',
            pn.layout.HSpacer(),
            collapse_button,
            css_classes=["card-header"],
        )
        super().__init__(
            header_row, content, **kwargs,
        )

    def clone(self, *objects, **params):
        # Hack. See https://github.com/holoviz/panel/issues/1060
        if objects:
            header, body = objects
            return super().clone(header.object, body, **params)

        return super().clone(**params)

    def _get_card_content(self, panels: List[pn.viewable.Viewable],) -> pn.viewable.Viewable:
        """Combines the list of Viewables into a Viewable with the right css classes

        Args:
            panels (List[pn.viewable.Viewable]): A list of Viewables

        Returns:
            pn.viewable.Viewable: A Viewable of the input Viewables with the right css classes \
                applied.
        """
        # Due to https://github.com/holoviz/panel/issues/903 we have to insert the content into a
        # column with relevant margin
        #
        content = pn.Column(
            *[self.get_card_panel(panel) for panel in panels],
            css_classes=["card-body"],
            sizing_mode="stretch_width",
            margin=(0, 2, 2, 0,),
        )
        # Due to Bokeh formatting every card-panel is 5px inside the card-body
        # and thus we cannot get borders to overlap.
        # So the first panel should have no border to hide this fact
        if len(content) > 0:
            if content[0].css_classes and "card-panel" in content[0].css_classes:
                content[0].css_classes.remove("card-panel")
                content[0].css_classes.append("card-panel-first")
            else:
                content[0].css_classes = ["card-panel-first"]
        return content

    @staticmethod
    def get_card_header(text: str, **kwargs,) -> pn.pane.HTML:
        """[summary]

        Arguments:
            text {str} -- A header string like 'Card Header'. May also contain HTML tags like <a>
            and <i>

        Returns:
            pn.pane.HTML -- The header text as a HTML Pane
        """
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
        """A Card Panel to be inserted into the body of the Card

        Arguments:
            obj {[type]} -- Any type that can be converted to a panel. An obj of type 'str' will
            always be converted to a HTML pane

        Returns:
            pn.viewable.Viewable -- A Viewable of the obj
        """
        if "css_classes" not in kwargs:
            kwargs["css_classes"] = []
        if "card-panel" not in kwargs["css_classes"]:
            kwargs["css_classes"].append("card-panel")
        if "sizing_mode" not in kwargs and "width" not in kwargs:
            kwargs["sizing_mode"] = "stretch_width"

        if isinstance(obj, str,):
            return pn.pane.Markdown(obj, **kwargs,)

        return pn.panel(obj, **kwargs,)
