import param
import panel as pn

class MyClass(param.Parameterized):
    def view(self):
        return pn.Column(
            "Hello World",
            pn.widgets.Button(name="Hello Me", width=250, button_type="success"),
            pn.widgets.Button(name="Button 1", width=250),
            sizing_mode="stretch_width",
        )