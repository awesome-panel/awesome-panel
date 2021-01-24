import panel as pn
import param

pn.extension()


class CustomTextInput(pn.widgets.TextInput):
    value_input = param.String(
        constant=True,
        doc="""
    Initial or current value.

    Change events are triggered whenever any update happens, i.e. on every
    keypress.
    """,
    )


txt = CustomTextInput(name="type here")
button = pn.widgets.Button(name="Submit", disabled=True)


@pn.depends(txt.param.value_input, watch=True)
def _update_button(value):
    button.disabled = len(value) <= 3


pn.Column(txt, button).servable()
