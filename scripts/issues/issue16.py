import markdown
import panel as pn

TEXT = """# Awesome Panel ![Awesome Badge](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)

Panel is announced as **a high-level app and dashboarding solution for Python**. I think the terms **powerfull** and **full of features** should be added to that.

The purpose of the Awesome Panel Project is to share knowledge on how Awesome Panel is and can become."""
CSS = """
p {
    width: 100%;
}
"""

pn.config.raw_css.append(CSS)

app_markdown = pn.Column(
    pn.pane.Markdown(TEXT, background="yellow",),
    pn.layout.HSpacer(),
    sizing_mode="stretch_width",
    background="blue",
)

app_markdown.servable()

app_html = pn.Column(
    pn.pane.HTML(TEXT, background="yellow",), sizing_mode="stretch_width", background="blue",
)

app_html.servable()

app_markdown_html = pn.Column(
    pn.pane.HTML(markdown.markdown(TEXT), background="yellow",),
    sizing_mode="stretch_width",
    background="blue",
)

app_markdown_html.servable()
