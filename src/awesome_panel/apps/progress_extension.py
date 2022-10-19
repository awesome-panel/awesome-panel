"""The ProgressExt widget enables easier progress reporting using the existing
[`pn.widgets.Progress`](https://panel.pyviz.org/reference/widgets/Progress.html#gallery-progress)
widget. It's available via the
[`awesome-panel-extensions`](https://pypi.org/project/awesome-panel-extensions/) package.

The ProgressExt widget provides

- A combination of a progress value and a progress message
- Easy to use functionality for
    - Function Annotation
    - Context Management

An example use case is

```python
import time

import panel as pn
from awesome_panel_extensions.widgets.progress_ext import ProgressExt

progress = ProgressExt()
run_button = pn.widgets.Button(name="Click me")

@progress.increment(50, "incrementing ...")
def run(event):
    time.sleep(0.5)
run_button.on_click(run)

app = pn.Column(run_button, progress.view)
app.servable()
```

This will show the progress bar and reset every 2 clicks.
"""

import time

import panel as pn
from awesome_panel_extensions.widgets.progress_ext import ProgressExt

from awesome_panel import config

config.extension(url="progress_extension", main_max_width="1000px")

pn.Column(
    """## Value and Message

We test the view with a value and a message

- The progress bar is active with the value 50
- The message hello world is visible
- The bar color is the blue *info* color
""",
    ProgressExt(
        value=50,
        message="hello world",
    ).view(),
).servable()


pn.Column(
    """# Message Only

We test the view with a message only

- The progress bar is active with no value
- The message is stated
- The bar color is the blue *info* color
""",
    ProgressExt(
        value=0,
        message="hello world",
    ).view(),
).servable()

pn.Column(
    """## Value only

We test the view with a value only

- The progressbar is shown with a value of 50
- No message is shown
""",
    ProgressExt(
        value=50,
        message="",
    ).view(),
)


pn.Column(
    """## No Message or Value

We test the view with no message or value

- No progressbar is shown
- No message is shown
""",
    ProgressExt(
        value=0,
        message="",
    ).view(),
).servable()


pn.Column(
    """## Bar Color

We test the view with a value and a message

- The progress bar is active with the value 50
- The message hello world is visible
- The bar color is the green *success* color
""",
    ProgressExt(
        value=50,
        message="hello world",
        bar_color="success",
    ).view(),
)


def _test_report_as_context_manager():
    progress = ProgressExt()
    run_button = pn.widgets.Button(name="Click me")

    def run(
        event,
    ):  # pylint: disable=unused-argument
        with progress.report(
            50,
            "running",
        ):
            time.sleep(1)

    run_button.on_click(run)
    return pn.Column(
        """## Context Manager

We test that the `ProgressExt.report` function works as a context manager

- Click the button to see the progress reported for 1 secs
""",
        run_button,
        progress.view,
    )


_test_report_as_context_manager().servable()


def _test_report_as_decorator():
    progress = ProgressExt()
    run_button = pn.widgets.Button(name="Click me")

    @progress.report(
        33,
        "calculation",
    )
    def run(
        event,
    ):  # pylint: disable=unused-argument
        time.sleep(1)

    run_button.on_click(run)
    return pn.Column(
        """## Decorator

We test that the `ProgressExt.report` function works as a decorator

- Click the button to see the progress reported for 1 secs
""",
        run_button,
        progress.view,
    )


_test_report_as_decorator().servable()


def _test_increment_as_context_manager():
    """We test that the `ProgressExt.report` function works as a context manager

    - Click the button multiple times and check that the progress is reset every 2 clicks
    """
    progress = ProgressExt()
    run_button = pn.widgets.Button(name="Click me")

    def run(
        event,
    ):  # pylint: disable=unused-argument
        with progress.increment(
            50,
            "incrementing ...",
        ):
            time.sleep(0.5)

    run_button.on_click(run)
    return pn.Column(
        """## Context Manager with increments

    We test that the `ProgressExt.report` function works as a context manager

    - Click the button multiple times and check that the progress is reset every 2 clicks
    """,
        run_button,
        progress.view,
    )


_test_increment_as_context_manager().servable()


def _test_increment_as_decorator():
    progress = ProgressExt()
    run_button = pn.widgets.Button(name="Click me")

    @progress.increment(
        50,
        "incrementing ...",
    )
    def run(
        event,
    ):  # pylint: disable=unused-argument
        time.sleep(0.5)

    run_button.on_click(run)
    return pn.Column(
        """## Decorator with increments

We test that the `ProgressExt.report` function works as a context manager

- Click the button multiple times and check that the progress is reset every 2 clicks
""",
        run_button,
        progress.view,
    )


_test_increment_as_decorator().servable()
