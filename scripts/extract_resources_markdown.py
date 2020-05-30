import pathlib
import sys

from awesome_panel.utils.resources import get_resources_markdown

ROOT = pathlib.Path(__file__).parent.parent
sys.path.append(str(ROOT))

from application.config.resources import RESOURCES


RESOURCES_MD = pathlib.Path.cwd() / "application/pages/resources/resources.md"
text = """# Awesome Panel Resources ![Awesome Badge](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)
""" + get_resources_markdown(RESOURCES, [])
RESOURCES_MD.write_text(text)
