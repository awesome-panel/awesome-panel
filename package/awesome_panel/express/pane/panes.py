"""A collection of nice panes to use"""

import panel as pn


class Code(pn.pane.Markdown):
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
        super().__init__(
            code_markdown, sizing_mode=sizing_mode, **kwargs,
        )
