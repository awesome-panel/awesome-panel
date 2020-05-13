"""This module implements a View to be used for viewing errors"""
import panel as pn

ERROR_VIEW_CLASS = "designer-error-view"
ERROR_MESSAGE_CLASS = "designer-error-message"
BACKGROUND = "#f8d7da"


class ErrorView(pn.Column):
    """The ErrorView displays the error_message nicely formatted

        Args:
            error_message (str): A stack trace or similar
            params: Parameters normally accepted by panel.Column

        """

    def __init__(self, error_message: str, **params):
        error = error_message
        error = f"""\
# Error

```bash
{error}
```
"""
        if params is None:
            params = {}
        if "css_classes" not in params:
            params["css_classes"] = []
        if not ERROR_VIEW_CLASS in params:
            params["css_classes"].append(ERROR_VIEW_CLASS)
        params["background"] = BACKGROUND
        if not "sizing_mode" in params:
            params["sizing_mode"] = "stretch_width"

        super().__init__(
            pn.pane.Markdown(error, margin=20, css_classes=[ERROR_MESSAGE_CLASS]), **params
        )
