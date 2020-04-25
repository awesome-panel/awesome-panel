import panel as pn


def get_content(title="App Title"):
    return pn.Column(
        "# " + title,
        pn.widgets.Button(name="Click me!", sizing_mode="stretch_width"),
        sizing_mode="stretch_width",
        background="lightgray",
    )


def app_body_margin_css():
    css = """
        body {
            margin-top: 0px;
            margin-bottom: 0px;
            margin-left: 20%;
            margin-right: 20%;
        }
    """
    pn.config.raw_css.append(css)
    content = get_content("App Body Margin CSS")
    return content


def app_margin():
    content = get_content("App Margin")
    content.margin = (0, 100, 0, 100)
    return content


def app_gridspec():
    gspec = pn.GridSpec(sizing_mode="stretch_width")
    gspec[:, 0] = pn.Spacer()
    gspec[:, 1:4] = get_content("App GridSpace")
    gspec[:, 4] = pn.Spacer()
    return gspec


app_body_margin_css().show()
