import panel as pn
import param


class MyComponent(param.Parameterized):
    selection1 = param.ObjectSelector()
    selection2 = param.ObjectSelector()


component = MyComponent()
app = pn.Column(
    pn.pane.Markdown("# Primary Selections"),
    pn.Param(component, parameters=["selection1"], show_name=False),
    pn.pane.Markdown("# Secondary Selections"),
    pn.Param(component, parameters=["selection2"], show_name=False),
)
app.show()
