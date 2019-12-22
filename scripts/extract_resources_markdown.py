import awesome_panel.core.services.resources as resources
import pathlib

RESOURCES_MD = pathlib.Path.cwd() / "src/pages/resources.md"
text = """# Awesome Panel Resources ![Awesome Badge](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)
""" + resources.get_resources_markdown(
    []
)
RESOURCES_MD.write_text(text)

