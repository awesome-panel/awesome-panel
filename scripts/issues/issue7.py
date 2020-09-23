import panel as pn


def main():
    text = """Navigate to the Dashboard Page via the Sidebar to see the result.
As you can see there is some friction in using markdown in Panel!
But Panel could be so awesome with just a bit of friction removed :-)"""
    app = pn.Column(
        pn.pane.Markdown(text),
        sizing_mode="stretch_width",
        background="#d1ecf1",
    )
    app.servable()


main()
