"""Component used by test_designer_app.py"""

import panel as pn
import param


class Component(param.Parameterized):
    """Dummy component for testing"""

    click_me = param.Action()
    select_me = param.ObjectSelector("b", ["a", "b"])
    view = param.Parameter(label="Test Component View")

    def __init__(self, **params):
        if "name" not in params:
            params["name"] = "Test Component"
        super().__init__(**params)

        self.view = pn.Column(
            pn.Param(self, parameters=["click_me", "select_me"]),
            name="Test Component Parameters",
        )
