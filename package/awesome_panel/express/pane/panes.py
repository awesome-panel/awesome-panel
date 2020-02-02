"""A collection of nice panes to use"""
import pathlib
from typing import Optional

import markdown
import panel as pn

from awesome_panel.express.assets import CODE_HILITE_PANEL_EXPRESS_CSS

MARKDOWN_EXTENSIONS = [
    "markdown.extensions.extra",
    "markdown.extensions.smarty",
    "fenced_code",
    "codehilite",
]

_EXTENDED = False


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
            text_with_no_leading_spaces, extensions=MARKDOWN_EXTENSIONS, output_format="html5",
        )

        super().__init__(
            text_html, **kwargs,
        )


class Code(pn.pane.HTML):
    """A HTML code block"""

    def __init__(
        self, code: str = "", language: str = "python", sizing_mode="stretch_width", **kwargs,
    ):
        """A HTML code block"""
        code_markdown = f"""
```{language}
{code}
```
"""
        code_html = markdown.markdown(
            code_markdown, extensions=MARKDOWN_EXTENSIONS, output_format="html5",
        )
        super().__init__(
            code_html, sizing_mode=sizing_mode, **kwargs,
        )

    @staticmethod
    def extend():
        """Adds Code Hilite CSS Formatting to the app"""
        global _EXTENDED  # pylint: disable=global-statement
        if not _EXTENDED:
            _EXTENDED = True
            pn.config.raw_css.append(CODE_HILITE_PANEL_EXPRESS_CSS.read_text())
