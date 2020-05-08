"""Component used by test_designer_app.py"""

import param
import panel as pn

class Component(param.Parameterized):
    click_me = param.Action()
    select_me = param.ObjectSelector("a", ["a", "b"])
    view = param.Parameter()

    def __init__(self, **params):
        super().__init__(**params)

        self.view = pn.Column(
            pn.Param(self, parameters=["click_me", "select_me"])
        )
