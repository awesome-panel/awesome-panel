import param
import panel as pn

MESSAGE = """\
# Stopped

Thanks for using the Panel Designer by awesome-panel.org
"""

class StoppedComponent(param.Parameterized):
    view = param.ClassSelector(class_=pn.pane.Markdown)
    def __init__(self, **params):
        super().__init__(**params)

        self.view = pn.pane.Markdown(MESSAGE)