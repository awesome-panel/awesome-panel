"""Exposes paths to assets"""
import pathlib

ROOT = pathlib.Path(__file__).parent
CSS_ROOT = ROOT / "css"
IMAGE_ROOT = ROOT / "images"

BOOTSTRAP_PANEL_EXPRESS_CSS = CSS_ROOT / "bootstrap_panel_express.css"
CODE_HILITE_PANEL_EXPRESS_CSS = CSS_ROOT / "code_hilite_panel_express.css"
SCROLLBAR_PANEL_EXPRESS_CSS = CSS_ROOT / "scrollbar_panel_express.css"
FONTAWESOME_PANEL_EXPRESS_CSS = CSS_ROOT / "fontawesome_panel_express.css"
LOADING_IO_PANEL_EXPRESS_CSS = CSS_ROOT / "loading_io_panel_express.css"
SPINNER_JPG = IMAGE_ROOT / "spinner-icon-gif-10.jpg"