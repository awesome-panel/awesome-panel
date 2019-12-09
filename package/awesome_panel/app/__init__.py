from panel.pane import Markdown


def title_awesome(body: str) -> Markdown:
    """Writes the title as f'Awesome Panel {body}'
    - plus the awesome badge
    - plus a link to the awesome-streamlit GitHub page

    Arguments:
        body {str} -- [description]

    Returns:
        Markdown -- A 'Awesome Panel {body} title with the awesome badge
    """
    return Markdown(
        f"# Awesome Panel {body} "
        "![Awesome Badge](https://cdn.rawgit.com/sindresorhus/awesome/"
        "d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)"
    )
