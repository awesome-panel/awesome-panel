"""The PageComponent is an abstract base class.

Don't use it directly. But use it for

- Creating SubClass implementations
- Creating PageComponents from other components
"""

import inspect

import param

from awesome_panel.application.models import Page, Progress, Toast


class PageComponent(param.Parameterized):
    """The PageComponent defines a page

Use it for

- Creating an instance by providing its parameters
- Creating SubClass implementations
- Creating PageComponents from many types of components via the `create` function
"""
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
    def create(cls, component) -> 'PageComponent':
        """Creates a PageComponent from the component

        This method

        Args:
            component Anything that is a Panel or Panel can convert to a Panel.

                - Also supports functions, classes and modules that have main, view and/ or sidebar
                attributes or functions.
                - If the object is already a PageComponent it is just returned.

        Returns:
            PageComponent: An instance of PageComponent
        """
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
