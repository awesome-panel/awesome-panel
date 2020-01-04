"""In this module we define the ProgressExt widget.

The purpose of the ProgressExt widget is to make the existing `pn.widgets.Progress` easier to use.

The ProgressExt does this by providing

- A combination of a progress value and a progress message
- Easy to use functions for
    - Annotatings
    - Context Management

To enable easy progress reporting from functions and parts of code.
"""
import param
import panel as pn
from contextlib import contextmanager


class ProgressExt(param.Parameterized):
    value = param.Integer(default=0)
    message = param.String(default="")
    bar_color = param.String(default="info")

    """The purpose of the ProgressExt widget is to make the existing `pn.widgets.Progress` easier to use.

    The ProgressExt does this by providing

    - A combination of a progress value and a progress message
    - Easy to use functions for
        - Annotatings
        - Context Management

    To enable easy progress reporting from functions and parts of code.
    """

    def update(self, value: int, message: str):
        # We need this to not trigger the Progress shows as active
        self.value = value
        self.message = message

    def reset(self):
        self.message=""
        self.value=0

    @param.depends("value", "message", "bar_color")
    def view(self) -> pn.pane.Viewable:
        content = []
        if self.value:
            content.append(
                pn.widgets.Progress(value=self.value, bar_color=self.bar_color, align="center")
            )
        elif self.message:
            content.append(
                pn.widgets.Progress(active=True, bar_color=self.bar_color, align="center")
            )
        if self.value and not self.message:
            content.append(pn.pane.Str(" ")) # Hack: To stop progressbar from jumping vertically
        if self.message:
            content.append(pn.pane.Str(self.message))
        return pn.Row(*content, sizing_mode="stretch_width")

    @contextmanager
    def report(self, value: int, message: str):
        self.update(value, message)
        yield
        self.reset()

    @contextmanager
    def increment(self, value: int, message: str):
        value_half = int(value/2)

        self.value = min(self.value + value_half, 100)
        self.message = message

        yield
        new_value = self.value + value - value_half
        if new_value >= 100:
            self.reset()
        else:
            self.value=new_value
