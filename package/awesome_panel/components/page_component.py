import inspect

import panel as pn
import param

from awesome_panel.models import Page, Progress, Toast


class PageComponent(param.Parameterized):
    page = param.ClassSelector(class_=Page)
    main = param.Parameter()
    sidebar = param.Parameter()
    progress = param.ClassSelector(class_=Progress)
    toast = param.ClassSelector(class_=Toast)

    def __init__(self, **params):
        if "progress" not in params:
            params["progress"] = Progress()
        if "toast" not in params:
            params["toast"] = Toast()

        super().__init__(**params)

    @classmethod
    def create(cls, component):
        if inspect.isclass(component):
            component = component()

        if issubclass(type(component), cls):
            return component

        if hasattr(component, "main"):
            main = component.main
        elif hasattr(component, "view"):
            main = component.view
        else:
            main = component
        if callable(main):
            main = main()

        if hasattr(component, "sidebar"):
            sidebar = component.sidebar
        else:
            sidebar = None
        if callable(sidebar):
            sidebar = sidebar()

        return cls(main=main, sidebar=sidebar)
