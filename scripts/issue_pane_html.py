import panel as pn
import param

STATIC = "<img src='https://github.com/MarcSkovMadsen/awesome-panel/raw/master/assets/images/spinners/spinner_panel_static_light_400_340.gif' style='height:100%' title=''></img>"
BREATH = "<img src='https://github.com/MarcSkovMadsen/awesome-panel/raw/master/assets/images/spinners/spinner_panel_breath_light_400_340.gif' style='height:100%' title=''></img>"


class Spinner(pn.pane.HTML):
    def __init__(self, **params):
        self.param.object.default = STATIC
        super().__init__(**params)

    def toggle(self, _=None):
        if self.object == STATIC:
            self.object = BREATH
        else:
            self.object = STATIC


spinner = Spinner()
button = pn.widgets.Button(name="Toggle")
button.on_click(spinner.toggle)

app = pn.Column(button, spinner.param.object, spinner, sizing_mode="stretch_both")
app.show()
