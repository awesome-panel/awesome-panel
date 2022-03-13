"""Module of paths to and text from Markdown files"""
import pathlib

ABOUT_PATH = pathlib.Path(__file__).parent / "about.md"
ABOUT_TEXT = ABOUT_PATH.read_text(encoding="utf8")

HOME_PATH = pathlib.Path(__file__).parent / "home.md"
HOME_TEXT = HOME_PATH.read_text(encoding="utf8")
