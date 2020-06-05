"""This module implements the CenteredComponent which can be used to center a component


"""
import panel as pn
import param


class CenteredComponent(pn.Column):
    """The CenteredComponent can be used to center a component"""

    component = param.Parameter()

    def __init__(self, component=None, **params):
        self._rename["component"] = None

        if "sizing_mode" not in params:
            params["sizing_mode"] = "stretch_both"

        super().__init__(**params)
        self.component = component

        self._spacer = pn.Spacer()
        self._vspacer = pn.layout.HSpacer(height=20)
        self._update()

    @param.depends("component", watch=True)
    def _update(self):
        if self.component is None:
            self[:] = [self._spacer]
            return

        component = self.component
        if isinstance(component, pn.reactive.Reactive):
            main_content = component
        elif hasattr(component, "view") and component.view:
            main_content = component.view
        else:
            raise NotImplementedError

        main_content.align = "center"
        if main_content.css_classes is None:
            main_content.css_classes = []
        if "designer-centered-component" not in main_content.css_classes:
            main_content.css_classes.append("designer-centered-component")
        main_content.margin = (10, 25, 10, 5)
        self[:] = [
            main_content,
            self._vspacer,
        ]

    def __repr__(self, depth=0, max_depth=0):
        return f"PanelDesigner({self.name})"

    def __str__(self):
        return f"PanelDesigner({self.name})"
