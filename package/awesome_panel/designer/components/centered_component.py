import param
import panel as pn

class CenteredComponent(pn.Column):
    component = param.Parameter()

    def __init__(self, component=None, **params):
        self._rename["component"]=None

        if "sizing_mode" not in params:
            params["sizing_mode"]="stretch_both"


        super().__init__(**params)
        self.component = component

        self._spacer = pn.Spacer()
        self._vspacer = pn.layout.HSpacer(height=20)
        self._update()


    @param.depends("component", watch=True)
    def _update(self):
        if self.component is None:
            self[:]=[self._spacer]
            return

        main_content = self.component
        main_content.align="center"
        if main_content.css_classes is None:
            main_content.css_classes = []
        if "designer-centered-component" not in main_content.css_classes:
            main_content.css_classes.append("designer-centered-component")
        main_content.margin = (10,25,10,5)
        self[:]=[
            main_content,
            self._vspacer,
        ]

    def __repr__(self):
        return f"PanelDesigner(self.__name__)"

    def __str__(self):
        return f"PanelDesigner(self.__name__)"