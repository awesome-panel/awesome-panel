"""A collection of nice panes to use"""
import pathlib
from typing import Optional

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
        self, code: str = "", language: str = "python", sizing_mode="stretch_width", **kwargs
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
        super().__init__(code_html, sizing_mode=sizing_mode, **kwargs)
