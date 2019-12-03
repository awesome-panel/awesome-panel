"""A collection of nice panes to use"""
from typing import List

import bokeh
import markdown
import panel as pn

MARKDOWN_EXTENSIONS = [
    "markdown.extensions.extra",
    "markdown.extensions.smarty",
    "fenced_code",
    "codehilite",
]


class Divider(pn.pane.HTML):
    """A HTML Divider"""

    def __init__(self, sizing_policy="stretch_width", *args, **kwargs):
        """A HTML Divider

        The HTML

        Arguments:
            pn {[type]} -- [description]

        Keyword Arguments:
            sizing_policy {str} -- [description] (default: {"stretch_width"})
        """
        super().__init__("<hr>", height=10, sizing_mode="stretch_width")


class Code(pn.pane.Markdown):
    """A HTML code block"""

    def __init__(
        self, code: str = "", language: str = "python", sizing_mode="stretch_width", *args, **kwargs
    ):
        """A HTML code block"""
        code_markdown = f"""
```{language}
{code}
```
"""
        code_html = markdown.markdown(
            code_markdown, extensions=MARKDOWN_EXTENSIONS, output_format="html5"
        )
        super().__init__(code_html, sizing_mode=sizing_mode, *args, **kwargs)


class InfoAlert(pn.pane.Markdown):
    """An Info Alert that renders Markdown

    CSS Styling can be done via the classes 'alert' and 'alert-info'. See the raw_css attribute

    Don't set sizing_mode="stretch_width" as this will result in problems.
    See https://github.com/holoviz/panel/issues/829
    """

    def __init__(
        self, text: str, css_classes: List[str] = ["alert", "alert-info"], *args, **kwargs,
    ):
        """An Info Alert that renders Markdown

        CSS Styling can be done via the classes 'alert' and 'alert-info'

        Arguments:
            text {str} -- Some MarkDown text

        KeyWord Arguments:
            css_classes {List[str]} --
        """
        super().__init__(text, css_classes=css_classes)

    raw_css = """
.bk.alert {
    position: relative;
    padding: 0.75rem 1.25rem;
    border: 1px solid transparent;
    border-radius: 0.25rem;
}

.bk.alert-info {
    color: #0c5460;
    background-color: #d1ecf1;
    border-color: #bee5eb;
}

.bk.alert-info hr {
    border-top-color: #abdde5;
}
"""


class WarningAlert(pn.pane.Markdown):
    """An Warning Alert that renders Markdown

    CSS Styling can be done via the classes 'alert' and 'alert-warning'. See the raw_css attribute

    Don't set sizing_mode="stretch_width" as this will result in problems.
    See https://github.com/holoviz/panel/issues/829
    """

    def __init__(
        self, text: str, css_classes: List[str] = ["alert", "alert-warning"], *args, **kwargs,
    ):
        """An Warning Alert that renders Markdown

        CSS Styling can be done via the classes 'alert' and 'alert-warning'

        Arguments:
            text {str} -- Some MarkDown text

        """
        super().__init__(text, css_classes=css_classes)

    raw_css = """
.bk.alert {
    position: relative;
    padding: 0.75rem 1.25rem;
    border: 1px solid transparent;
    border-radius: 0.25rem;
}

.bk.alert-warning {
    color: #856404;
    background-color: #fff3cd;
    border-color: #ffeeba;
}

.bk.alert-warning hr {
    border-top-color: #ffe8a1;
}
"""


class ErrorAlert(pn.pane.Markdown):
    """An Error Alert that renders Markdown

    CSS Styling can be done via the classes 'alert' and 'alert-error'. See the raw_css attribute

    Don't set sizing_mode="stretch_width" as this will result in problems.
    See https://github.com/holoviz/panel/issues/829
    """

    def __init__(
        self, text: str, css_classes: List[str] = ["alert", "alert-error"], *args, **kwargs,
    ):
        """An Error Alert that renders Markdown

        CSS Styling can be done via the classes 'alert' and 'alert-error'

        Arguments:
            text {str} -- Some MarkDown text

        """
        super().__init__(text, css_classes=css_classes)

    raw_css = """
.bk.alert {
    position: relative;
    padding: 0.75rem 1.25rem;
    border: 1px solid transparent;
    border-radius: 0.25rem;
}

.bk.alert-error {
    color: #721c24;
    background-color: #f8d7da;
    border-color: #f5c6cb;
}

.bk.alert-error hr {
    border-top-color: #f1b0b7;
}
"""
