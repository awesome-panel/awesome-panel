import panel as pn


def main():
    text_error = """
    This is not formatted correctly by Markdown due to the indentation!"""
    text_ok = """
This is formatted correctly by Markdown!
"""
    app = pn.Column(
        pn.pane.Markdown(text_error),
        pn.pane.HTML("<hr>", sizing_mode="stretch_width"),
        pn.pane.Markdown(text_ok),
    )
    app.servable()


main()
