import panel as pn

TEMPLATE = """
{% extends base %}

<!-- goes in head -->
{% block postamble %}
<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
{% endblock %}

<!-- goes in body -->
{% block contents %}
{{ embed(roots.body) }}

{% endblock %}
"""

CSS = """\
body{
    margin: 0px;
    background: pink;
    overflow-x: hidden;
    overflow-y: hidden;
    width: 100%;
}
.bk.header{
    color: white;
    background-color: black;

    position: -webkit-sticky; /* Safari */
    position: sticky !important;
    top: 0;

    box-shadow: 5px 5px 20px grey;

    z-index: 1000;
}
.bk.app-title a{
    color: white;
    background-color: black;
    text-align: center;
    font-size: 1rem;
}
.bk.app-title a:link {
    text-decoration: none;
}
.bk.app-title a:hover{
    color: white;
}
.bk.sidebar{
    background-color: rgb(248, 249, 250);

    height: 100vh !important;

    position: -webkit-sticky; /* Safari */
    position: sticky !important;
    top: 58px !important;

    overflow-x: hidden;
    overflow-y: auto;
}
.bk.content{
    background-color: white;
    /* hack: Had to set overflow-x to hidden in order to not get scrollbar on About Page */
    overflow-x: hidden;
    overflow-y: auto;
}
"""

ABOUT = """\
# About

[Panel](https://panel.pyviz.org/) is a pwerful framework for building awesome-analytics apps in [Python](https://www.python.org/).

The purpose of this app is to test that a **multi-page Dashboard Layout** similar to the [bootstrap dashboard template](https://getbootstrap.com/docs/4.3/examples/dashboard/) from [getboostrap.com](https://getbootstrap.com/) can be implemented in [Panel](https://panel.pyviz.org/).
"""

IMAGE = "https://getbootstrap.com/docs/4.4/assets/img/examples/dashboard.png"

INFO = """\
Navigate to the **Dashboard Page** via the **Sidebar** to see the result.
Or Navigate to the **Limitations Page** to learn of some of the limitations of Panel that
I've experienced."""

SIDEBAR_WIDTH = 300


def main():
    pn.config.raw_css.append(CSS)

    app_title = pn.Row(
        pn.layout.HSpacer(),
        pn.pane.Markdown(f"Bootstrap Dashboard"),
        pn.layout.HSpacer(),
        width=SIDEBAR_WIDTH,
        css_classes=["app-title"],
    )
    header = pn.Row(
        app_title, pn.layout.HSpacer(), sizing_mode="stretch_width", css_classes=["header"],
    )
    sidebar = pn.Column(
        "Sidebar",
        pn.layout.HSpacer(height_policy="max"),
        height_policy="max",
        width=SIDEBAR_WIDTH,
        css_classes=["sidebar"],
    )
    content = pn.Column(width_policy="max", margin=(25, 50, 25, 50,), css_classes=["content"],)

    about = pn.layout.Row(pn.pane.Markdown(ABOUT))
    image = pn.pane.PNG(IMAGE)
    info = pn.pane.Markdown(INFO, background="#d1ecf1",)
    page = pn.Column(about, image, info, sizing_mode="stretch_width", css_classes=["about"],)

    content.append(page)

    body = pn.Column(
        header, pn.Row(sidebar, content,), sizing_mode="stretch_width", background="darkgray",
    )

    items = {
        "body": body,
    }
    template = pn.Template(template=TEMPLATE, items=items,)
    template.servable()


if __name__.startswith("bokeh"):
    main()
