"""Exposes Paths to the following assets

- BOOTSTRAP_PANEL_EXPRESS_CSS
- CODE_HILITE_PANEL_EXPRESS_CSS
- SCROLLBAR_PANEL_EXPRESS_CSS
- FONTAWESOME_PANEL_EXPRESS_CSS
"""
import pathlib

ROOT = pathlib.Path(__file__).parent
CSS_ROOT = ROOT / "css"
IMAGE_ROOT = ROOT / "images"

BOOTSTRAP_PANEL_EXPRESS_CSS = CSS_ROOT / "bootstrap_panel_express.css"
CODE_HILITE_PANEL_EXPRESS_CSS = CSS_ROOT / "code_hilite_panel_express.css"
SCROLLBAR_PANEL_EXPRESS_CSS = CSS_ROOT / "scrollbar_panel_express.css"
FONTAWESOME_PANEL_EXPRESS_CSS = CSS_ROOT / "fontawesome_panel_express.css"
