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
        if "page" not in params:
            raise ValueError("No `page` provided!")
        if "progress" not in params:
            params["progress"] = Progress()
        if "toast" not in params:
            params["toast"] = Toast()

        super().__init__(**params)
