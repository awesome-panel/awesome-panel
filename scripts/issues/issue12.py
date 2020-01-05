import panel as pn
import param

PAGES = {
    "About": pn.pane.Markdown("about " * 2500, sizing_mode="stretch_width", name="About"),
    "Holoviews": pn.pane.Markdown(
        "holoviews " * 2500, sizing_mode="stretch_width", name="Holoviews"
    ),
    "Plotly": pn.pane.Markdown("plotly " * 2500, sizing_mode="stretch_width", name="Plotly"),
}

CSS = """\
body {
    margin: 0px;
    width: 100vh-500px;
}
"""


def main() -> pn.Pane:
    pn.config.raw_css.append(CSS)
    navigator = pn.widgets.RadioBoxGroup(name="RadioBoxGroup", options=list(PAGES))
    sidebar = pn.Column(navigator, pn.layout.VSpacer(), width=300, background="lightgray")
    tabs = pn.layout.Tabs(name="Tabs")
    content = pn.Column(PAGES["About"], sizing_mode="stretch_both")

    def page(event):
        print("---------")
        print(event)
        print(PAGES[event.new])
        content.clear()
        content.append(PAGES[event.new])

    navigator.param.watch(page, "value")

    app = pn.Row(sidebar, content, sizing_mode="stretch_both")
    return app


if __name__.startswith("bk_script"):
    main().servable()
