import panel as pn
import panel.widgets


def main():
    buttons1 = [pn.widgets.Button(name=f"{i}") for i in range(0, 5,)]
    example1 = pn.WidgetBox(
        *buttons1, background="blue", sizing_mode="stretch_width", name="Example 1",
    )
    buttons2 = [pn.widgets.Button(name=f"{i}", max_width=50,) for i in range(0, 5,)]
    example2 = pn.WidgetBox(*buttons2, background="green", width=100, name="Example 2",)
    app = pn.Column(example1, example2, sizing_mode="stretch_width",)
    app.servable()


main()
