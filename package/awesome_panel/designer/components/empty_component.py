import panel as pn
import param

class EmptyComponent(param.Parameterized):
    view = param.ClassSelector(class_=pn.Column)
    def __init__(self, **params):
        super().__init__(**params)

        view = pn.Column("# Empty Component")