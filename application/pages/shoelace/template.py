"""Custom Panel Template With a Dialog"""
import pathlib

import panel as pn
import param

TEMPLATE = (pathlib.Path(__file__).parent / "template.html").read_text()


class TemplateWithDialog(pn.template.Template):
    """Custom Panel Template With a Dialog"""

    dialog_open = param.Action()
    dialog_close = param.Action()

    # TEMPLATE = (pathlib.Path(__file__).parent / "template.html").read_text()

    def __init__(self, header, main, dialog, dialog_label: str):
        super().__init__(
            template=TEMPLATE,
        )

        self.add_panel("header", header)
        self.add_panel("main", main)
        self.add_panel("dialog", dialog)
        self.add_variable("dialog_label", dialog_label)
