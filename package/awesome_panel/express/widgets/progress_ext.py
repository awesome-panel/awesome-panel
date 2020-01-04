"""In this module we define the ProgressExt widget.

The purpose of the ProgressExt widget is to make the existing `pn.widgets.Progress` easier to use.

The ProgressExt does this by providing

- A combination of a progress value and a progress message
- Easy to use functions for
    - Annotatings
    - Context Management

To enable easy progress reporting from functions and parts of code.

An example use case is

```python
progress = ProgressExt()
run_button = pn.widgets.Button(name="Click me")

@progress.increment(50, "incrementing ...")
def run(event):
    time.sleep(0.5)
run_button.on_click(run)

app = pn.Column(run_button, progress.view)
app.servable()
```

which will show the progress and reset every 2 clicks.
"""
from contextlib import contextmanager

import panel as pn
import param


class ProgressExt(param.Parameterized):
    """The purpose of the ProgressExt widget is to enable easier progress reporting using the
    existing [`pn.widgets.Progress`]\
    (https://panel.pyviz.org/reference/widgets/Progress.html#gallery-progress) widget.

    The ProgressExt widget provides

    - A combination of a progress value and a progress message
    - Easy to use functionality for
        - Function Annotation
        - Context Management

    An example use case is

    ```python
    progress = ProgressExt()
    run_button = pn.widgets.Button(name="Click me")

    @progress.increment(50, "incrementing ...")
    def run(event):
        time.sleep(0.5)
    run_button.on_click(run)

    app = pn.Column(run_button, progress.view)
    app.servable()
    ```

    which will show the progress and reset every 2 clicks.
    """

    value = param.Integer(default=0)
    message = param.String(default="")
    bar_color = param.String(default="info")

    def update(self, value: int, message: str):
        """Updates the value and message

        Args:
            value (int): A value between 0 and 100
            message (str): A message for the user describing what is happening
        """
        # Please note the order matters as the Widgets updates two times. One for each change
        self.value = value
        self.message = message

    def reset(self):
        """Resets the value and message"""
        # Please note the order matters as the Widgets updates two times. One for each change
        self.message = ""
        self.value = 0

    @param.depends("value", "message", "bar_color")
    def view(self) -> pn.pane.Viewable:
        """View the widget

        Returns:
            pn.pane.Viewable: Add this to your app to see the progress reported
        """
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
            content.append(pn.pane.Str(" "))  # Hack: To stop progressbar from jumping vertically
        if self.message:
            content.append(pn.pane.Str(self.message))
        return pn.Row(*content, sizing_mode="stretch_width")

    @contextmanager
    def report(self, value: int = 0, message: str = ""):
        """Report the value and message.

        When the function or code is finished the progress is reset.

        Can be used as context manager or decorator.

        Args:
            value (int, optional): A value between 0 and 100. Default is 0.
            message (str, optional): A message for the user describing what is happening. Default
            is ""

        Yields:
            None: Nothing is yielded
        """
        self.update(value, message)
        yield
        self.reset()

    @contextmanager
    def increment(self, value: int, message: str):
        """Increment the value and report the message.

        When the function or code is finished the progress is NOT reset unless self.value >= 100.

        Can be used as context manager or decorator.

        Args:
            value (int): A value between 0 and 100 that will be added to selv.value.
            message (str): A message for the user describing what is happening

        Yields:
            None: Nothing is yielded
        """
        value_half = int(value / 2)

        self.value = min(self.value + value_half, 100)
        self.message = message

        yield
        new_value = self.value + value - value_half
        if new_value >= 100:
            self.reset()
        else:
            self.value = new_value
