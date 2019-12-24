"""Functionality for awesome-streamlit.org"""
from panel.pane import Markdown


def title_awesome(body: str) -> Markdown:
    """An *Awesome Panel* title as a Markdown with

    - the text like 'Awesome Panel About'
    - the [Awesome Badge](https://cdn.rawgit.com/sindresorhus/awesome/\
d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)

    Arguments:
        body (str): Some title like 'About'

    Returns:
        Markdown: An 'Awesome Panel {body} title with a link and the awesome badge.
    """
    return Markdown(
        f"# Awesome Panel {body} "
        "![Awesome Badge](https://cdn.rawgit.com/sindresorhus/awesome/"
        "d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)"
    )
