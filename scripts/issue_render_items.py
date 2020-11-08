import panel as pn


def _create_app():
    view = pn.pane.Markdown("App View")
    app = pn.template.MaterialTemplate()
    app.main[:] = [view]  # There might be a list of elements

    # Something done automatically for all apps in the site
    info_card = pn.pane.Markdown("Info Card")
    app.main.insert(0, info_card)
    return app


def test_app():
    app = _create_app()
    main_items = [item[0] for item in app._render_items.values() if "main" in item[1]]

    assert main_items[0].object == "Info Card"
    assert main_items[1].object == "App View"
    assert main_items == list(app.main[:])


if __name__.startswith("bokeh"):
    _create_app().servable()
