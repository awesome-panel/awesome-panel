import panel as pn
import pathlib
from typing import Optional


class Markdown(pn.pane.Markdown):
    def __init__(self, text: str = "", path: Optional[pathlib.Path] = None, *args, **kwargs):
        if text == "" and path:
            text = path.read_text()

        super().__init__(text, *args, **kwargs)
