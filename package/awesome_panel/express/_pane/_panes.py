"""A collection of nice panes to use"""
import pathlib
from typing import List, Optional

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

    def __init__(self, sizing_mode="stretch_width", **kwargs):
        """A HTML Divider

        The HTML

        Arguments:
            pn {[type]} -- [description]

        Keyword Arguments:
            sizing_policy {str} -- [description] (default: {"stretch_width"})
        """
        super().__init__("<hr>", height=10, sizing_mode=sizing_mode, **kwargs)


class Markdown(pn.pane.HTML):
    """Extension of the original Markdown pane

    Can

    - Take path input
    - Remove leading spaces
    - Syntax highlight code
    """

    def __init__(
        self, text: str = "", path: Optional[pathlib.Path] = None, **kwargs,
    ):
        """Extension of the original Markdow pane

        Can

        - Take path input
        - Remove leading spaces
        - Syntax highlight code

        Keyword Arguments:
            text {str} -- The text to convert to Markdown (default: {""})
            path {Optional[pathlib.Path]} -- An optional path to a file (default: {None})
        """
        if text == "" and path:
            text = path.read_text()

        text_with_no_leading_spaces = "\n".join([line.lstrip() for line in text.splitlines()])

        text_html = markdown.markdown(
            text_with_no_leading_spaces, extensions=MARKDOWN_EXTENSIONS, output_format="html5"
        )

        super().__init__(text_html, **kwargs)


class Code(pn.pane.HTML):
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


class InfoAlert(Markdown):
    """An Info Alert that renders Markdown

    CSS Styling can be done via the classes 'alert' and 'alert-info'. See the raw_css attribute

    Don't set sizing_mode="stretch_width" as this will result in problems.
    See https://github.com/holoviz/panel/issues/829
    """

    def __init__(
        self, text: str, *args, **kwargs,
    ):
        """An Info Alert that renders Markdown

        CSS Styling can be done via the classes 'alert' and 'alert-info'

        Arguments:
            text {str} -- Some MarkDown text

        """
        if "css_classes" in kwargs:
            if not "alert" in kwargs["css_classes"]:
                kwargs["css_classes"].append("alert")
            if not "alert-info" in kwargs["css_classes"]:
                kwargs["css_classes"].append("alert-info")
        else:
            kwargs["css_classes"] = ["alert", "alert-info"]
        super().__init__(text, *args, **kwargs)

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
        self, text: str, *args, **kwargs,
    ):
        """An Warning Alert that renders Markdown

        CSS Styling can be done via the classes 'alert' and 'alert-warning'

        Arguments:
            text {str} -- Some MarkDown text

        """
        if "css_classes" in kwargs:
            if not "alert" in kwargs["css_classes"]:
                kwargs["css_classes"].append("alert")
            if not "alert-warning" in kwargs["css_classes"]:
                kwargs["css_classes"].append("alert-warning")
        else:
            kwargs["css_classes"] = ["alert", "alert-warning"]
        print(kwargs)
        super().__init__(text, *args, **kwargs)

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
    See [Issue 829](https://github.com/holoviz/panel/issues/829)
    """

    def __init__(
        self, text: str, *args, **kwargs,
    ):
        """An Error Alert that renders Markdown

        CSS Styling can be done via the classes 'alert' and 'alert-error'

        Arguments:
            text {str} -- Some MarkDown text

        """
        if "css_classes" in kwargs:
            if not "alert" in kwargs["css_classes"]:
                kwargs["css_classes"].append("alert")
            if not "alert-error" in kwargs["css_classes"]:
                kwargs["css_classes"].append("alert-error")
        else:
            kwargs["css_classes"] = ["alert", "alert-error"]
        super().__init__(text, *args, **kwargs)

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
