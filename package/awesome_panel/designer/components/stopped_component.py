"""This module implements the StoppedComponent. The view of the StoppedComponent is shown to the
user when he/ she exits the Designer"""
import panel as pn
import param

MESSAGE = """\
# Stopped

Thanks for using the Panel Designer by awesome-panel.org
"""


class StoppedComponent(param.Parameterized):
    """The viewStoppedComponent is shown to the user when he/ she exits the Designer"""

    view = param.ClassSelector(class_=pn.pane.Markdown)

    def __init__(self, **params):
        super().__init__(**params)

        self.view = pn.pane.Markdown(MESSAGE)
