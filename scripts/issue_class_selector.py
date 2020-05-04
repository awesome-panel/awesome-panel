import param


class Theme(param.Parameterized):
    pass


class ProgressSpinnerComponent(param.Parameterized):
    theme = param.ClassSelector(class_=Theme, instantiate=True)

    def __init__(self, **params):
        if "theme" not in params:
            params["theme"] = Theme()
        super().__init__(**params)


progress_spinner_component = ProgressSpinnerComponent()
assert isinstance(progress_spinner_component.theme, Theme)
