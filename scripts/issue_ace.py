import panel as pn
import param

pn.extension("ace")

class Editor(param.Parameterized):
    code = param.String("print('Hello World')")
    update_count = param.Integer(0)
    view = param.Parameter()

    def __init__(self, **params):
        super().__init__(**params)

        self.view = pn.Param(self, parameters=["code", "update_count"], widgets={"code": pn.widgets.TextAreaInput})

    @param.depends("code", watch=True)
    def _update_count(self):
        self.update_count+=1

Editor().view.servable()