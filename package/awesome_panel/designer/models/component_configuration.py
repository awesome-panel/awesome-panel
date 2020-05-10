import pathlib

import param


class ComponentConfiguration(param.Parameterized):
    component = param.ClassSelector(class_=param.Parameterized, is_instance=False, instantiate=False)
    css_path = param.ClassSelector(class_=pathlib.Path)
    js_path = param.ClassSelector(class_=pathlib.Path)
    parameters = param.Dict()

    def __str__(self):
        return f"ComponentConfiguration({self.name})"

    def __repr__(self):
        return f"ComponentConfiguration({self.name})"
