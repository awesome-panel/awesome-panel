from typing import List
import panel as pn
import param


class Navigator(param.Parameterized):
    active = param.ObjectSelector()

    def __init__(self, pages, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pages = pages
        self.params()["active"].objects = pages
        self.active = pages[0]

    def view(self) -> pn.Pane:
        def set_active(event):
            self.active = [page for page in self.pages if page.name == event.obj.name][0]

        menuitems = []
        for page in self.pages:
            button = pn.widgets.Button(name=page.name)
            button.on_click(set_active)
            menuitems.append(button)

        return pn.WidgetBox(
            *menuitems, sizing_mode="stretch_width", css_classes=["select-active-page"]
        )

    @param.depends("active")
    def view_active(self):
        # Hack Cannot return self.active
        return pn.Column(self.active, sizing_mode="stretch_width")
